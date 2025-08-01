# Strong No Recoil Application

A powerful anti-recoil and rapid fire utility for gaming applications, featuring a modern dark UI and comprehensive configuration options.

## Features

### 🎯 Anti-Recoil System
- **Strong recoil compensation** with adjustable vertical and horizontal strength
- **Multiple modes**: Light, Medium, and Heavy presets
- **Customizable delay** for precise timing
- **ADS requirement** option (Aim Down Sight)

### 🔥 Rapid Fire System
- **Adjustable fire rate** for different weapons
- **Synchronized with recoil control**
- **ADS requirement** option

### ⚙️ Configuration Management
- **Save/Load configurations** in multiple slots (1-10)
- **Preset modes** for quick setup
- **Real-time status monitoring**

### 🎨 Modern UI
- **Dark theme** with professional gaming aesthetic
- **Intuitive controls** with sliders and checkboxes
- **Status indicators** for active features

## Installation

### Prerequisites
- Python 3.7 or higher
- Windows 10/11 (for mouse and keyboard input)

### Setup
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python no_recoil_app.py
   ```

## Usage

### Basic Setup
1. **Launch the application**
2. **Select a mode** (LIGHT, MEDIUM, HEAVY)
3. **Enable features**:
   - Check "TOGGLE RECOIL SCRIPT" for anti-recoil
   - Check "TOGGLE RAPID FIRE SCRIPT" for rapid fire
4. **Adjust settings**:
   - **Vertical Strength**: Controls upward recoil compensation (0-15)
   - **Horizontal Strength**: Controls side-to-side recoil compensation (0-10)
   - **Delay**: Time between recoil adjustments (0.001-0.1 seconds)
   - **Speed**: Rapid fire timing in milliseconds (10-200ms)

### Advanced Configuration
- **Require ADS**: Enable to only activate when aiming down sights (right mouse button)
- **Configuration Slots**: Save up to 10 different configurations
- **Real-time Adjustment**: Modify settings while the application is running

### Mode Presets
- **LIGHT**: Gentle recoil control (Vertical: 3, Horizontal: 1, Delay: 0.02s)
- **MEDIUM**: Balanced recoil control (Vertical: 6, Horizontal: 2, Delay: 0.015s)
- **HEAVY**: Strong recoil control (Vertical: 8, Horizontal: 2, Delay: 0.01s)

## Controls

### Application Controls
- **START/STOP**: Toggle the recoil and rapid fire systems
- **LOAD CONFIG**: Load saved configuration from selected slot
- **SAVE CONFIG**: Save current settings to selected slot
- **EXIT**: Close the application

### In-Game Controls
- **Left Mouse Button**: Triggers recoil compensation and rapid fire
- **Right Mouse Button**: Required for ADS mode (if enabled)

## Safety Features

- **Thread-safe operation** with proper cleanup
- **Error handling** for input detection
- **Graceful shutdown** when closing the application
- **CPU optimization** with minimal resource usage

## Configuration Files

The application saves configurations as JSON files:
- `config_1.json` through `config_10.json`
- Automatically created when saving configurations
- Can be manually edited for advanced customization

## Troubleshooting

### Common Issues
1. **Application not responding**: Ensure you're running as administrator
2. **Input not detected**: Check if your game allows external input
3. **Performance issues**: Reduce delay values or disable unused features

### Performance Tips
- Use **LIGHT** mode for better performance
- Disable **rapid fire** if not needed
- Increase **delay** values for smoother operation

## Legal Notice

⚠️ **Important**: This application is for educational and testing purposes only. Users are responsible for ensuring compliance with:
- Game terms of service
- Local laws and regulations
- Fair play policies

The developers are not responsible for any consequences resulting from the use of this software.

## Technical Details

### Dependencies
- `pynput`: Mouse and keyboard input detection
- `keyboard`: Advanced keyboard input handling
- `mouse`: Mouse movement and click simulation
- `tkinter`: GUI framework (included with Python)

### Architecture
- **Multi-threaded design** for responsive UI
- **Event-driven input detection** for real-time response
- **Modular configuration system** for easy customization

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure proper permissions (run as administrator if needed)

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Compatibility**: Windows 10/11, Python 3.7+ 