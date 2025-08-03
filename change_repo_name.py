import webbrowser
import subprocess
import os

def change_repo_name():
    """Help user change repository name to get a new URL"""
    
    print("🔗 CHANGE GITHUB PAGES URL")
    print("=" * 50)
    
    print("\n📋 OPTIONS TO CHANGE URL:")
    print("1. Rename repository (easiest)")
    print("2. Create new repository")
    print("3. Use custom domain")
    
    print("\n🎯 RECOMMENDED: Rename Repository")
    print("Current URL: https://malam66.github.io/strong-no-recoil/")
    
    # Open GitHub repository settings
    print("\n🌐 Opening GitHub repository settings...")
    webbrowser.open('https://github.com/Malam66/strong-no-recoil/settings')
    
    print("\n📝 STEPS TO RENAME:")
    print("1. Click 'General' in the left menu")
    print("2. Find 'Repository name' section")
    print("3. Change 'strong-no-recoil' to your new name")
    print("4. Click 'Rename'")
    print("5. Your new URL will be: https://malam66.github.io/NEW-NAME/")
    
    print("\n💡 SUGGESTED NAMES:")
    print("- no-recoil-app")
    print("- gaming-utility")
    print("- recoil-control")
    print("- strong-app")
    
    print("\n⚠️  IMPORTANT:")
    print("- Repository must stay PUBLIC")
    print("- GitHub Pages will automatically update")
    print("- Old URL will redirect to new one")

if __name__ == "__main__":
    change_repo_name() 