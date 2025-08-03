#!/usr/bin/env python3
"""
Test script for Strong No Recoil Application
This will check if all components work properly
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import tkinter as tk
        print("✅ Tkinter imported successfully")
    except ImportError as e:
        print(f"❌ Tkinter import failed: {e}")
        return False
    
    try:
        from tkinter import ttk, messagebox
        print("✅ Tkinter components imported successfully")
    except ImportError as e:
        print(f"❌ Tkinter components import failed: {e}")
        return False
    
    try:
        import json
        print("✅ JSON imported successfully")
    except ImportError as e:
        print(f"❌ JSON import failed: {e}")
        return False
    
    try:
        import threading
        print("✅ Threading imported successfully")
    except ImportError as e:
        print(f"❌ Threading import failed: {e}")
        return False
    
    try:
        import time
        print("✅ Time imported successfully")
    except ImportError as e:
        print(f"❌ Time import failed: {e}")
        return False
    
    # Test optional imports
    try:
        from pynput import mouse, keyboard
        print("✅ Pynput imported successfully")
    except ImportError as e:
        print(f"⚠️  Pynput not available: {e}")
        print("   This is needed for mouse/keyboard input")
    
    try:
        import keyboard as kb
        print("✅ Keyboard module imported successfully")
    except ImportError as e:
        print(f"⚠️  Keyboard module not available: {e}")
        print("   This is needed for input detection")
    
    try:
        import mouse as ms
        print("✅ Mouse module imported successfully")
    except ImportError as e:
        print(f"⚠️  Mouse module not available: {e}")
        print("   This is needed for mouse movement")
    
    return True

def test_basic_app():
    """Test if the basic app can be imported"""
    print("\n🔍 Testing basic app...")
    
    try:
        # Import the basic app
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from no_recoil_app import NoRecoilApp
        print("✅ Basic app imported successfully")
        return True
    except Exception as e:
        print(f"❌ Basic app import failed: {e}")
        return False

def test_advanced_app():
    """Test if the advanced app can be imported"""
    print("\n🔍 Testing advanced app...")
    
    try:
        # Import the advanced app
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from advanced_no_recoil import AdvancedNoRecoilApp
        print("✅ Advanced app imported successfully")
        return True
    except Exception as e:
        print(f"❌ Advanced app import failed: {e}")
        return False

def test_launcher():
    """Test if the launcher can be imported"""
    print("\n🔍 Testing launcher...")
    
    try:
        # Import the launcher
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from launcher import NoRecoilLauncher
        print("✅ Launcher imported successfully")
        return True
    except Exception as e:
        print(f"❌ Launcher import failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Strong No Recoil - Application Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Basic imports failed. Please check Python installation.")
        return False
    
    # Test apps
    basic_ok = test_basic_app()
    advanced_ok = test_advanced_app()
    launcher_ok = test_launcher()
    
    print("\n📊 Test Results:")
    print(f"Basic App: {'✅ PASS' if basic_ok else '❌ FAIL'}")
    print(f"Advanced App: {'✅ PASS' if advanced_ok else '❌ FAIL'}")
    print(f"Launcher: {'✅ PASS' if launcher_ok else '❌ FAIL'}")
    
    if basic_ok and advanced_ok and launcher_ok:
        print("\n🎉 All tests passed! Your app should work properly.")
        print("\nTo run the app:")
        print("1. python launcher.py")
        print("2. python no_recoil_app.py")
        print("3. python advanced_no_recoil.py")
        return True
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n💡 Troubleshooting tips:")
        print("1. Make sure Python 3.7+ is installed")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Run as administrator if needed")
    
    input("\nPress Enter to exit...") 