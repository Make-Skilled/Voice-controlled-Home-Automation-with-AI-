# 🎤 Voice-Controlled Home Automation with AI

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.3.3-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
</div>

## 🌟 Overview

A cutting-edge voice-controlled home automation dashboard featuring AI-powered speech recognition, stunning cyberpunk UI design, and realistic virtual smart devices. Control your smart home with natural language commands through an immersive futuristic interface.

### ✨ Key Features

- 🎤 **AI Voice Recognition** - Natural language processing for intuitive commands
- 🎨 **Cyberpunk UI** - Glassmorphism effects with neon animations
- 🏠 **Virtual Devices** - 5 realistic smart home devices with animations
- ⚡ **Real-time Control** - Instant device responses and visual feedback
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🔊 **Audio Feedback** - Visual speech recognition indicators
- 📋 **Command Logging** - Real-time command history and status

## 🎯 Demo

### Virtual Devices Available:
1. **💡 Smart Bulb** - Brightness control with realistic glow effects
2. **🌀 Ceiling Fan** - 3-speed rotation with animated blades  
3. **❄️ Air Conditioner** - Temperature control (16-30°C)
4. **📺 Smart TV** - Volume control with screen effects
5. **🎵 Music System** - Volume control with beat animations

## 🛠️ Prerequisites

### System Requirements
- **Operating System:** Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18+)
- **Python:** Version 3.7 or higher
- **Browser:** Chrome or Edge (for full voice support)
- **Microphone:** Required for voice commands
- **RAM:** Minimum 4GB recommended
- **Internet:** Required for CDN resources

### Check Python Installation
```bash
python --version
# or
python3 --version
```
> If Python is not installed, download from [python.org](https://www.python.org/downloads/)

## 🚀 Quick Start Guide

### Step 1: Clone or Download Project

**Option A: Clone Repository (if using Git)**
```bash
git clone <repository-url>
cd voice-home-automation
```

**Option B: Manual Download**
1. Download all project files
2. Create a new folder named `voice-home-automation`
3. Place all files in the folder

### Step 2: Project Structure Setup

Create the following folder structure:
```
voice-home-automation/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates folder
│   └── index.html        # Main dashboard
└── static/              # Optional: Additional assets
```

**Create templates folder:**
```bash
mkdir templates
```

### Step 3: Virtual Environment Setup (Recommended)

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) in your command prompt
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) in your terminal
```

### Step 4: Install Dependencies

```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

**Expected output:**
```
Installing collected packages: Werkzeug, MarkupSafe, Jinja2, itsdangerous, click, blinker, Flask, Flask-CORS
Successfully installed Flask-2.3.3 Flask-CORS-4.0.0 ...
```

### Step 5: Verify Installation

```bash
# Check if Flask is installed
pip list | grep Flask

# Expected output:
# Flask                    2.3.3
# Flask-CORS               4.0.0
```

### Step 6: Run the Application

```bash
# Start the Flask server
python app.py
```

**Expected output:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
```

### Step 7: Access Dashboard

1. Open your web browser (Chrome or Edge recommended)
2. Navigate to: `http://localhost:5000`
3. Allow microphone permissions when prompted
4. Click the microphone button to start voice control!

## 🎤 Voice Commands Guide

### Device Control Commands

#### 💡 Smart Bulb
```
"Turn on the bulb"
"Turn off the light"  
"Set brightness to 75"
"Increase brightness"
"Decrease brightness"
```

#### 🌀 Ceiling Fan
```
"Turn on the fan"
"Turn off the ceiling fan"
"Set fan speed to 3"
"Fan speed medium"
"Fan speed high"
"Fan speed low"
```

#### ❄️ Air Conditioner
```
"Turn on the AC"
"Turn off air conditioner"
"Set temperature to 22 degrees"
"AC temperature 18"
```

#### 📺 Smart TV
```
"Turn on the TV"
"Turn off television"
"TV on"
"TV off"
```

#### 🎵 Music System
```
"Turn on music"
"Turn off speaker"
"Start music"
"Stop music"
```

### Usage Tips
- Speak clearly and at normal pace
- Wait for microphone activation (button turns green)
- Use natural language - the AI understands context
- Check command log for feedback and status

## 🔧 Manual Controls

Each device also has manual slider controls:
- **Bulb:** Brightness slider (0-100%)
- **Fan:** Speed slider (0-3 levels)
- **AC:** Temperature slider (16-30°C)
- **TV:** Volume slider (0-100%)
- **Music:** Volume slider (0-100%)

## 🎨 UI Features

### Visual Effects
- **Glassmorphism Cards** - Frosted glass effect with blur
- **Neon Glow** - Dynamic lighting and shadows
- **Animated Grid** - Moving cyberpunk background
- **Device Animations** - Realistic device behaviors
- **Status Indicators** - Real-time device status lights

### Interactive Elements
- **Voice Button** - Animated microphone with pulse effect
- **Speech Wave** - Visual audio input indicator  
- **Command Log** - Real-time command history
- **Hover Effects** - Smooth card interactions

## 🐛 Troubleshooting

### Common Issues

#### 1. "Python not found" Error
```bash
# Try python3 instead of python
python3 app.py

# Or add Python to PATH (Windows)
# Add Python installation directory to system PATH
```

#### 2. "pip not found" Error
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux  
python3 -m pip install -r requirements.txt
```

#### 3. Speech Recognition Not Working
- **Solution:** Use Chrome or Edge browser
- **Check:** Microphone permissions are allowed
- **Verify:** Microphone is working in other applications

#### 4. Port Already in Use
```bash
# If port 5000 is busy, specify different port in app.py
# Change last line to:
app.run(debug=True, port=5001)

# Then access: http://localhost:5001
```

#### 5. Templates Not Found Error
```bash
# Ensure templates folder exists and contains index.html
mkdir templates
# Copy index.html to templates folder
```

#### 6. CORS Issues
- The Flask-CORS package should handle this
- If issues persist, try accessing via `127.0.0.1:5000` instead of `localhost:5000`

### Performance Issues

#### Slow Loading
- Check internet connection (CDN resources needed)
- Try refreshing the page
- Clear browser cache

#### Voice Recognition Delays
- Ensure stable internet connection
- Close other applications using microphone
- Try speaking closer to microphone

## 🌐 Browser Compatibility

| Browser | Voice Recognition | Visual Features | Overall Support |
|---------|------------------|-----------------|-----------------|
| Chrome | ✅ Full Support | ✅ Full Support | ✅ Recommended |
| Edge | ✅ Full Support | ✅ Full Support | ✅ Recommended |
| Firefox | ❌ Limited | ✅ Full Support | ⚠️ Partial |
| Safari | ❌ No Support | ✅ Full Support | ⚠️ Visual Only |

## 📱 Device Compatibility

- **Desktop:** Full functionality
- **Laptop:** Full functionality  
- **Tablet:** Touch controls work, voice support varies
- **Mobile:** Basic functionality, limited voice support

## 🔒 Security & Privacy

### Local Data Only
- All processing happens locally
- No data sent to external servers
- Voice commands processed in browser

### Development Mode
- Currently in debug mode for development
- For production use, disable debug mode
- Add authentication for public deployment

## 🚀 Deployment Options

### Local Network Access
```python
# In app.py, change last line to:
app.run(debug=True, host='0.0.0.0', port=5000)

# Access from other devices: http://YOUR_IP:5000
```

### Cloud Deployment
- **Heroku:** Add `Procfile` and `runtime.txt`
- **AWS:** Use Elastic Beanstalk or EC2
- **Digital Ocean:** Use App Platform
- **Vercel/Netlify:** For static deployment

## 🔄 Updates & Maintenance

### Updating Dependencies
```bash
# Activate virtual environment first
pip install --upgrade -r requirements.txt
```

### Adding New Devices
1. Update `device_states` in `app.py`
2. Add device parsing in `parse_voice_command()`
3. Create device visual in HTML/CSS
4. Add control logic in JavaScript

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

### Code Style
- Follow PEP 8 for Python code
- Use consistent JavaScript formatting
- Comment complex functions
- Test voice commands thoroughly

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

### Getting Help
- Check troubleshooting section first
- Search existing issues
- Create new issue with details:
  - Operating system
  - Python version  
  - Browser used
  - Error messages
  - Steps to reproduce

### Feature Requests
- Open GitHub issue
- Describe use case
- Provide implementation suggestions

## 🎉 Acknowledgments

- **Flask** - Web framework
- **Web Speech API** - Voice recognition
- **Tailwind CSS** - Styling framework
- **Font Awesome** - Icons
- **Google Fonts** - Typography

---

<div align="center">
  <p>Made with ❤️ for the future of home automation</p>
  <p>⭐ Star this project if you found it helpful!</p>
</div>