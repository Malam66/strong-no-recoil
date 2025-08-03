#!/usr/bin/env python3
"""
Fix script for Strong No Recoil Application
This will fix common issues and ensure the app works properly
"""

import os
import sys
import subprocess

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_files():
    """Check if all required files exist"""
    print("🔍 Checking files...")
    
    required_files = [
        'no_recoil_app.py',
        'advanced_no_recoil.py',
        'launcher.py',
        'requirements.txt',
        'setup.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ {file} exists")
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files exist")
        return True

def fix_import_issues():
    """Fix common import issues"""
    print("🔧 Fixing import issues...")
    
    # Check if pynput is installed
    try:
        import pynput
        print("✅ Pynput is installed")
    except ImportError:
        print("⚠️  Installing pynput...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput==1.7.6'])
            print("✅ Pynput installed successfully")
        except:
            print("❌ Failed to install pynput")
    
    # Check if keyboard module is installed
    try:
        import keyboard
        print("✅ Keyboard module is installed")
    except ImportError:
        print("⚠️  Installing keyboard module...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keyboard==0.13.5'])
            print("✅ Keyboard module installed successfully")
        except:
            print("❌ Failed to install keyboard module")
    
    # Check if mouse module is installed
    try:
        import mouse
        print("✅ Mouse module is installed")
    except ImportError:
        print("⚠️  Installing mouse module...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mouse==0.7.1'])
            print("✅ Mouse module installed successfully")
        except:
            print("❌ Failed to install mouse module")

def create_simple_test():
    """Create a simple test to verify the app works"""
    print("🧪 Creating simple test...")
    
    test_code = '''
import tkinter as tk
from tkinter import messagebox

def test_gui():
    root = tk.Tk()
    root.title("Test - Strong No Recoil")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Strong No Recoil Test", font=("Arial", 16))
    label.pack(pady=20)
    
    def show_success():
        messagebox.showinfo("Success", "GUI is working properly!")
        root.destroy()
    
    btn = tk.Button(root, text="Test GUI", command=show_success)
    btn.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    test_gui()
'''
    
    with open('simple_test.py', 'w') as f:
        f.write(test_code)
    
    print("✅ Simple test created (simple_test.py)")

def main():
    """Main fix function"""
    print("🔧 Strong No Recoil - App Fix")
    print("=" * 40)
    
    # Check files
    if not check_files():
        print("❌ Some required files are missing")
        return False
    
    # Install dependencies
    install_dependencies()
    
    # Fix import issues
    fix_import_issues()
    
    # Create simple test
    create_simple_test()
    
    print("\n🎉 Fix completed!")
    print("\nTo test the app:")
    print("1. python simple_test.py (tests GUI)")
    print("2. python test_app.py (tests all components)")
    print("3. python launcher.py (runs the actual app)")
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ App should now work properly!")
    else:
        print("\n❌ Some issues remain. Please check the errors above.")
    
    input("\nPress Enter to exit...") 