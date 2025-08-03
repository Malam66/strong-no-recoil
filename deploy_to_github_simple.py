import os
import subprocess
import webbrowser

def deploy_to_github():
    """Deploy the website to GitHub Pages"""
    
    print("🚀 DEPLOYING TO GITHUB PAGES")
    print("=" * 50)
    
    # Check if git is initialized
    if not os.path.exists('.git'):
        print("❌ Git not initialized. Please run these commands:")
        print("git init")
        print("git add .")
        print("git commit -m 'Initial commit'")
        return
    
    # Check if remote is set
    result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
    if not result.stdout.strip():
        print("❌ No GitHub repository connected.")
        print("\n📋 TO SET UP GITHUB:")
        print("1. Go to: https://github.com/new")
        print("2. Create repository: 'strong-no-recoil'")
        print("3. Make it PUBLIC")
        print("4. Run these commands:")
        print("   git remote add origin https://github.com/YOUR_USERNAME/strong-no-recoil.git")
        print("   git branch -M main")
        print("   git push -u origin main")
        return
    
    # Add all files
    print("📁 Adding files...")
    subprocess.run(['git', 'add', '.'])
    
    # Commit changes
    print("💾 Committing changes...")
    subprocess.run(['git', 'commit', '-m', 'Update website with simple download design'])
    
    # Push to GitHub
    print("🚀 Pushing to GitHub...")
    result = subprocess.run(['git', 'push'], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("\n✅ SUCCESS! Website deployed to GitHub!")
        print("\n🌐 NEXT STEPS:")
        print("1. Go to your GitHub repository")
        print("2. Click 'Settings'")
        print("3. Scroll to 'Pages' section")
        print("4. Select 'Deploy from a branch'")
        print("5. Choose 'main' branch")
        print("6. Click 'Save'")
        print("\n⏰ Wait 5-10 minutes for deployment")
        print("🌍 Your website will be at: https://YOUR_USERNAME.github.io/strong-no-recoil")
        
        # Open GitHub in browser
        webbrowser.open('https://github.com')
    else:
        print("❌ Error pushing to GitHub:")
        print(result.stderr)

if __name__ == "__main__":
    deploy_to_github() 