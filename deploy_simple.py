#!/usr/bin/env python3
"""
Simple deployment script for Strong No Recoil Website
"""

import webbrowser
import os

def main():
    """Main deployment function"""
    print("🚀 Strong No Recoil - Simple Deployment")
    print("=" * 40)
    
    print("❌ The Problem:")
    print("You're getting a 404 error because your website isn't on GitHub yet.")
    print()
    
    print("✅ The Solution:")
    print("Follow these steps to deploy your website:")
    print()
    
    print("Step 1: Create GitHub Repository")
    print("1. Go to: https://github.com/new")
    print("2. Repository name: strong-no-recoil")
    print("3. Make it Public ✅")
    print("4. Don't check 'Add a README file'")
    print("5. Click 'Create repository'")
    print()
    
    print("Step 2: Upload Files")
    print("1. Download GitHub Desktop: https://desktop.github.com/")
    print("2. Install and open GitHub Desktop")
    print("3. Clone your repository")
    print("4. Copy ALL files from your folder to the repository folder")
    print("5. Commit and push (click 'Commit to main' then 'Push origin')")
    print()
    
    print("Step 3: Enable GitHub Pages")
    print("1. Go to your repository on GitHub")
    print("2. Click 'Settings' (top menu)")
    print("3. Scroll down to 'Pages' section")
    print("4. Under 'Source', select 'Deploy from a branch'")
    print("5. Select 'main' branch")
    print("6. Click 'Save'")
    print()
    
    print("Step 4: Fix Username")
    print("1. Double-click fix_username.bat")
    print("2. Enter your GitHub username when prompted")
    print("3. Commit and push the changes")
    print()
    
    print("🌐 Your Website URL:")
    print("After completing the steps above, your website will be at:")
    print("https://YOUR_USERNAME.github.io/strong-no-recoil")
    print()
    
    print("⏰ Timeline:")
    print("- 2 minutes: Create repository")
    print("- 3 minutes: Upload files")
    print("- 1 minute: Enable GitHub Pages")
    print("- 5 minutes: Website live")
    print()
    
    # Ask if user wants to open GitHub
    response = input("Would you like to open GitHub to create the repository? (y/n): ")
    if response.lower() == 'y':
        webbrowser.open('https://github.com/new')
        print("✅ GitHub opened!")
    
    print()
    print("💡 Alternative: View Locally")
    print("To see your website right now:")
    print("1. Double-click index.html")
    print("2. Or double-click open_website_simple.bat")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...") 