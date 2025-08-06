from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re
import json

app = Flask(__name__)
CORS(app)

# Device states
device_states = {
    'bulb': {'status': 'off', 'brightness': 50},
    'fan': {'status': 'off', 'speed': 1},
    'ac': {'status': 'off', 'temperature': 22},
    'tv': {'status': 'off', 'volume': 30},
    'music': {'status': 'off', 'volume': 50}
}

def parse_voice_command(command):
    """Parse voice command and extract device and action"""
    command = command.lower().strip()
    
    # Device keywords
    devices = {
        'bulb': ['bulb', 'light', 'lamp'],
        'fan': ['fan', 'ceiling fan'],
        'ac': ['ac', 'air conditioner', 'air conditioning'],
        'tv': ['tv', 'television', 'telly'],
        'music': ['music', 'speaker', 'audio']
    }
    
    # Action keywords
    actions = {
        'on': ['on', 'turn on', 'switch on', 'start'],
        'off': ['off', 'turn off', 'switch off', 'stop'],
        'increase': ['increase', 'up', 'higher', 'more', 'louder'],
        'decrease': ['decrease', 'down', 'lower', 'less', 'quieter']
    }
    
    detected_device = None
    detected_action = None
    
    # Find device
    for device, keywords in devices.items():
        if any(keyword in command for keyword in keywords):
            detected_device = device
            break
    
    # Find action
    for action, keywords in actions.items():
        if any(keyword in command for keyword in keywords):
            detected_action = action
            break
    
    # Special cases for fan speed
    if detected_device == 'fan':
        speed_match = re.search(r'speed (\d+)', command)
        if speed_match:
            return detected_device, 'set_speed', int(speed_match.group(1))
        
        if any(word in command for word in ['slow', 'low']):
            return detected_device, 'set_speed', 1
        elif any(word in command for word in ['medium', 'med']):
            return detected_device, 'set_speed', 2
        elif any(word in command for word in ['fast', 'high', 'max']):
            return detected_device, 'set_speed', 3
    
    # Special cases for brightness
    if detected_device == 'bulb':
        brightness_match = re.search(r'brightness (\d+)', command)
        if brightness_match:
            return detected_device, 'set_brightness', int(brightness_match.group(1))
    
    # Special cases for temperature
    if detected_device == 'ac':
        temp_match = re.search(r'(\d+) degree', command)
        if temp_match:
            return detected_device, 'set_temperature', int(temp_match.group(1))
        temp_match2 = re.search(r'ac temperature (\d+)', command)
        if temp_match2:
            return detected_device, 'set_temperature', int(temp_match2.group(1))

    # TV volume voice commands
    if detected_device == 'tv':
        vol_match = re.search(r'volume (\d+)', command)
        if vol_match:
            return detected_device, 'set_volume', int(vol_match.group(1))
        if detected_action in ['increase', 'decrease']:
            return detected_device, detected_action, 'volume'

    # Music volume voice commands
    if detected_device == 'music':
        vol_match = re.search(r'volume (\d+)', command)
        if vol_match:
            return detected_device, 'set_volume', int(vol_match.group(1))
        if detected_action in ['increase', 'decrease']:
            return detected_device, detected_action, 'volume'

    return detected_device, detected_action, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/devices', methods=['GET'])
def get_devices():
    return jsonify(device_states)

@app.route('/api/command', methods=['POST'])
def process_command():
    data = request.json
    command = data.get('command', '')
    
    device, action, value = parse_voice_command(command)
    
    if not device:
        return jsonify({'error': 'Device not recognized', 'command': command})
    
    if device not in device_states:
        return jsonify({'error': 'Device not found', 'command': command})
    
    response = {'device': device, 'action': action, 'command': command}
    
    # Execute action
    if action == 'on':
        device_states[device]['status'] = 'on'
        response['message'] = f'{device.capitalize()} turned on'

    elif action == 'off':
        device_states[device]['status'] = 'off'
        response['message'] = f'{device.capitalize()} turned off'

    elif action == 'set_speed' and device == 'fan' and value is not None:
        device_states[device]['speed'] = max(1, min(3, value))
        device_states[device]['status'] = 'on'
        response['message'] = f'Fan speed set to {device_states[device]["speed"]}'

    elif action == 'set_brightness' and device == 'bulb' and value is not None:
        device_states[device]['brightness'] = max(0, min(100, value))
        device_states[device]['status'] = 'on' if value > 0 else 'off'
        response['message'] = f'Bulb brightness set to {device_states[device]["brightness"]}%'

    elif action == 'set_temperature' and device == 'ac' and value is not None:
        device_states[device]['temperature'] = max(16, min(30, value))
        device_states[device]['status'] = 'on'
        response['message'] = f'AC temperature set to {device_states[device]["temperature"]}°C'

    elif action == 'set_volume' and device in ['tv', 'music'] and value is not None:
        device_states[device]['volume'] = max(0, min(100, value))
        device_states[device]['status'] = 'on' if value > 0 else 'off'
        response['message'] = f'{device.capitalize()} volume set to {device_states[device]["volume"]}%'

    elif action == 'increase' and value == 'volume' and device in ['tv', 'music']:
        device_states[device]['volume'] = min(100, device_states[device]['volume'] + 10)
        device_states[device]['status'] = 'on' if device_states[device]['volume'] > 0 else 'off'
        response['message'] = f'{device.capitalize()} volume increased to {device_states[device]["volume"]}%'

    elif action == 'decrease' and value == 'volume' and device in ['tv', 'music']:
        device_states[device]['volume'] = max(0, device_states[device]['volume'] - 10)
        device_states[device]['status'] = 'on' if device_states[device]['volume'] > 0 else 'off'
        response['message'] = f'{device.capitalize()} volume decreased to {device_states[device]["volume"]}%'

    else:
        response['error'] = 'Action not recognized or not applicable'
        response['message'] = 'Command not understood'

    response['devices'] = device_states
    return jsonify(response)

@app.route('/api/device/<device>', methods=['POST'])
def control_device(device):
    """Manual device control endpoint"""
    data = request.json
    
    if device not in device_states:
        return jsonify({'error': 'Device not found'})
    
    if 'status' in data:
        device_states[device]['status'] = data['status']
    
    if 'speed' in data and device == 'fan':
        device_states[device]['speed'] = max(1, min(3, data['speed']))
    
    if 'brightness' in data and device == 'bulb':
        device_states[device]['brightness'] = max(0, min(100, data['brightness']))
    
    if 'temperature' in data and device == 'ac':
        device_states[device]['temperature'] = max(16, min(30, data['temperature']))
    
    if 'volume' in data and device in ['tv', 'music']:
        device_states[device]['volume'] = max(0, min(100, data['volume']))
    
    return jsonify({'device': device, 'state': device_states[device]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)