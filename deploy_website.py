#!/usr/bin/env python3
"""
Deploy Strong No Recoil Website to GitHub Pages
This script will help you deploy your website step by step
"""

import os
import subprocess
import webbrowser
import time

def check_git():
    """Check if Git is installed"""
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        print("✅ Git is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed")
        print("Please install Git from: https://git-scm.com/")
        return False

def check_github_cli():
    """Check if GitHub CLI is installed"""
    try:
        subprocess.run(['gh', '--version'], check=True, capture_output=True)
        print("✅ GitHub CLI is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  GitHub CLI is not installed")
        print("You can install it from: https://cli.github.com/")
        return False

def create_repository():
    """Create GitHub repository using GitHub CLI"""
    if not check_github_cli():
        print("\n📋 Manual Repository Creation:")
        print("1. Go to https://github.com/new")
        print("2. Repository name: strong-no-recoil")
        print("3. Make it Public")
        print("4. Don't initialize with README")
        print("5. Click 'Create repository'")
        return False
    
    print("\n🚀 Creating GitHub repository...")
    try:
        # Create repository
        subprocess.run(['gh', 'repo', 'create', 'strong-no-recoil', '--public', '--source=.', '--remote=origin', '--push'], check=True)
        print("✅ Repository created and files pushed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create repository: {e}")
        return False

def setup_git():
    """Setup Git repository"""
    print("🔧 Setting up Git repository...")
    
    # Initialize Git if not already done
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'], check=True)
        print("✅ Git repository initialized")
    
    # Add all files
    subprocess.run(['git', 'add', '.'], check=True)
    print("✅ Files added to Git")
    
    # Commit files
    subprocess.run(['git', 'commit', '-m', 'Initial commit - Strong No Recoil Website'], check=True)
    print("✅ Files committed")

def enable_github_pages():
    """Enable GitHub Pages"""
    print("\n🌐 Enabling GitHub Pages...")
    
    if check_github_cli():
        try:
            # Enable GitHub Pages
            subprocess.run(['gh', 'api', 'repos/:owner/:repo/pages', '--method', 'POST', '--field', 'source=gh-pages'], check=True)
            print("✅ GitHub Pages enabled!")
            return True
        except subprocess.CalledProcessError:
            print("⚠️  Could not enable GitHub Pages automatically")
    
    print("\n📋 Manual GitHub Pages Setup:")
    print("1. Go to your repository on GitHub")
    print("2. Click 'Settings' tab")
    print("3. Scroll down to 'Pages' section")
    print("4. Under 'Source', select 'Deploy from a branch'")
    print("5. Select 'gh-pages' branch")
    print("6. Click 'Save'")
    return False

def create_gh_pages_branch():
    """Create gh-pages branch for GitHub Pages"""
    print("🌿 Creating gh-pages branch...")
    
    try:
        # Create and switch to gh-pages branch
        subprocess.run(['git', 'checkout', '-b', 'gh-pages'], check=True)
        
        # Push gh-pages branch
        subprocess.run(['git', 'push', 'origin', 'gh-pages'], check=True)
        print("✅ gh-pages branch created and pushed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create gh-pages branch: {e}")
        return False

def update_download_js():
    """Update download.js with actual GitHub username"""
    print("🔧 Updating download.js...")
    
    # Get GitHub username
    try:
        result = subprocess.run(['gh', 'api', 'user', '--jq', '.login'], capture_output=True, text=True, check=True)
        username = result.stdout.strip()
        print(f"✅ Found GitHub username: {username}")
        
        # Update download.js
        with open('download.js', 'r') as f:
            content = f.read()
        
        content = content.replace('YOUR_USERNAME', username)
        
        with open('download.js', 'w') as f:
            f.write(content)
        
        print("✅ download.js updated with your username")
        return True
    except:
        print("⚠️  Could not automatically update download.js")
        print("Please manually replace 'YOUR_USERNAME' with your actual GitHub username in download.js")
        return False

def main():
    """Main deployment function"""
    print("🚀 Strong No Recoil - Website Deployment")
    print("=" * 50)
    
    # Check requirements
    if not check_git():
        return False
    
    # Setup Git
    setup_git()
    
    # Update download.js
    update_download_js()
    
    # Create repository
    if create_repository():
        # Create gh-pages branch
        create_gh_pages_branch()
        
        # Enable GitHub Pages
        enable_github_pages()
        
        print("\n🎉 Deployment completed!")
        print("\n📱 Your website will be available at:")
        print("https://YOUR_USERNAME.github.io/strong-no-recoil")
        print("\n⏳ It may take a few minutes for the site to be live")
        
        # Ask if user wants to open the website
        response = input("\nWould you like to open the website? (y/n): ")
        if response.lower() == 'y':
            webbrowser.open('https://YOUR_USERNAME.github.io/strong-no-recoil')
    else:
        print("\n📋 Manual Deployment Steps:")
        print("1. Create repository on GitHub")
        print("2. Push your files to GitHub")
        print("3. Enable GitHub Pages in repository settings")
        print("4. Your website will be live at: https://YOUR_USERNAME.github.io/strong-no-recoil")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...") 