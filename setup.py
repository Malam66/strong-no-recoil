#!/usr/bin/env python3
"""
Strong No Recoil Setup Script
Automatically installs dependencies and sets up the application
"""

import subprocess
import sys
import os
import platform

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ ERROR: Python 3.7 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False
    except FileNotFoundError:
        print("❌ requirements.txt not found!")
        return False

def check_dependencies():
    """Check if all dependencies are installed"""
    required_packages = ['pynput', 'keyboard', 'mouse']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is missing")
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages

def create_desktop_shortcut():
    """Create desktop shortcut for easy access"""
    try:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        shortcut_path = os.path.join(desktop_path, "Strong No Recoil.bat")
        
        with open(shortcut_path, 'w') as f:
            f.write('@echo off\n')
            f.write('cd /d "%~dp0"\n')
            f.write('python launcher.py\n')
            f.write('pause\n')
        
        print("✅ Desktop shortcut created!")
        return True
    except Exception as e:
        print(f"❌ Failed to create desktop shortcut: {e}")
        return False

def main():
    print("🚀 Strong No Recoil Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        input("\nPress Enter to exit...")
        return
    
    # Check current dependencies
    deps_ok, missing = check_dependencies()
    
    if not deps_ok:
        print(f"\nMissing packages: {', '.join(missing)}")
        choice = input("Install missing dependencies? (y/n): ").lower()
        if choice == 'y':
            if not install_dependencies():
                input("\nPress Enter to exit...")
                return
        else:
            print("❌ Setup cancelled")
            input("\nPress Enter to exit...")
            return
    else:
        print("\n✅ All dependencies are already installed!")
    
    # Create desktop shortcut
    choice = input("\nCreate desktop shortcut? (y/n): ").lower()
    if choice == 'y':
        create_desktop_shortcut()
    
    print("\n🎉 Setup completed successfully!")
    print("\nTo run the application:")
    print("1. Double-click 'run_launcher.bat'")
    print("2. Or run: python launcher.py")
    print("3. Or use the desktop shortcut (if created)")
    
    # Launch option
    choice = input("\nLaunch the application now? (y/n): ").lower()
    if choice == 'y':
        try:
            subprocess.Popen([sys.executable, 'launcher.py'])
        except Exception as e:
            print(f"❌ Failed to launch: {e}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main() 