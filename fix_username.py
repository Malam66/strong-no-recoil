#!/usr/bin/env python3
"""
Fix GitHub Username in download.js
This script will help you replace YOUR_USERNAME with your actual GitHub username
"""

def fix_username():
    """Replace YOUR_USERNAME with actual GitHub username"""
    print("🔧 Fix GitHub Username in download.js")
    print("=" * 40)
    
    # Get username from user
    username = input("Enter your GitHub username: ").strip()
    
    if not username:
        print("❌ Username cannot be empty!")
        return False
    
    # Read the file
    try:
        with open('download.js', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ download.js not found!")
        return False
    
    # Replace YOUR_USERNAME with actual username
    new_content = content.replace('YOUR_USERNAME', username)
    
    # Write back to file
    with open('download.js', 'w') as f:
        f.write(new_content)
    
    print(f"✅ Updated download.js with username: {username}")
    print(f"🌐 Your website will be at: https://{username}.github.io/strong-no-recoil")
    
    return True

def show_instructions():
    """Show manual instructions"""
    print("\n📋 Manual Instructions:")
    print("1. Open download.js in a text editor")
    print("2. Replace all instances of 'YOUR_USERNAME' with your actual GitHub username")
    print("3. Save the file")
    print("4. Upload to GitHub")
    print("5. Your website will be at: https://YOUR_USERNAME.github.io/strong-no-recoil")

def main():
    """Main function"""
    print("🎯 Fix GitHub Username")
    print("=" * 30)
    
    choice = input("Do you want to automatically fix the username? (y/n): ").lower()
    
    if choice == 'y':
        if fix_username():
            print("\n🎉 Username fixed!")
            print("Now upload your files to GitHub and enable GitHub Pages.")
        else:
            show_instructions()
    else:
        show_instructions()
    
    print("\n💡 Next steps:")
    print("1. Create GitHub repository: strong-no-recoil")
    print("2. Upload all files")
    print("3. Enable GitHub Pages")
    print("4. Your website will be live!")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...") 