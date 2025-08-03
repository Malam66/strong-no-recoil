#!/usr/bin/env python3
"""
Automated GitHub Deployment Script for Strong No Recoil
This script will help you deploy your project to GitHub automatically.
"""

import subprocess
import sys
import os
import getpass

def run_command(command, description=""):
    """Run a command and handle errors"""
    print(f"🔄 {description}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Success")
            return True
        else:
            print(f"❌ {description} - Failed")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} - Exception: {e}")
        return False

def check_git_status():
    """Check if we have a clean git repository"""
    print("🔍 Checking Git status...")
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print("⚠️  You have uncommitted changes. Committing them...")
        run_command("git add .", "Adding all files")
        run_command("git commit -m \"Auto-commit before GitHub deployment\"", "Committing changes")
    else:
        print("✅ Repository is clean")

def get_github_username():
    """Get GitHub username from user"""
    print("\n📝 GitHub Setup")
    print("=" * 40)
    username = input("Enter your GitHub username: ").strip()
    if not username:
        print("❌ Username cannot be empty")
        return None
    return username

def create_github_repository(username):
    """Create GitHub repository using GitHub CLI or provide instructions"""
    print(f"\n🚀 Creating GitHub repository for user: {username}")
    
    # Check if GitHub CLI is installed
    if run_command("gh --version", "Checking GitHub CLI"):
        print("✅ GitHub CLI found - attempting automatic repository creation")
        
        # Create repository using GitHub CLI
        repo_name = "strong-no-recoil"
        description = "A powerful anti-recoil and rapid fire utility for gaming applications"
        
        create_cmd = f'gh repo create {repo_name} --description "{description}" --public --source=. --remote=origin --push'
        
        if run_command(create_cmd, "Creating GitHub repository"):
            print("🎉 Repository created and code pushed successfully!")
            return True
        else:
            print("⚠️  Automatic creation failed, providing manual instructions")
    else:
        print("ℹ️  GitHub CLI not found, providing manual instructions")
    
    return False

def provide_manual_instructions(username):
    """Provide manual instructions for GitHub setup"""
    print("\n📋 Manual GitHub Setup Instructions")
    print("=" * 50)
    print("1. Go to https://github.com/new")
    print("2. Repository name: strong-no-recoil")
    print("3. Description: A powerful anti-recoil and rapid fire utility for gaming applications")
    print("4. Make it Public or Private (your choice)")
    print("5. DO NOT initialize with README (we already have one)")
    print("6. Click 'Create repository'")
    print("\nAfter creating the repository, run these commands:")
    print(f"git remote add origin https://github.com/{username}/strong-no-recoil.git")
    print("git branch -M main")
    print("git push -u origin main")
    
    choice = input("\nHave you created the repository? (y/n): ").lower()
    if choice == 'y':
        return setup_remote_and_push(username)
    else:
        print("⏸️  Please create the repository first, then run this script again")
        return False

def setup_remote_and_push(username):
    """Set up remote and push to GitHub"""
    print(f"\n🔗 Setting up remote for {username}")
    
    # Add remote
    if not run_command(f"git remote add origin https://github.com/{username}/strong-no-recoil.git", "Adding remote"):
        print("⚠️  Remote might already exist, continuing...")
    
    # Rename branch to main
    run_command("git branch -M main", "Renaming branch to main")
    
    # Push to GitHub
    if run_command("git push -u origin main", "Pushing to GitHub"):
        print("🎉 Successfully deployed to GitHub!")
        print(f"🌐 Your repository: https://github.com/{username}/strong-no-recoil")
        return True
    else:
        print("❌ Failed to push to GitHub")
        return False

def main():
    """Main deployment function"""
    print("🚀 Strong No Recoil - GitHub Deployment")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists(".git"):
        print("❌ Not in a git repository. Please run 'git init' first.")
        return False
    
    # Check git status
    check_git_status()
    
    # Get GitHub username
    username = get_github_username()
    if not username:
        return False
    
    # Try automatic creation first
    if not create_github_repository(username):
        # Fall back to manual instructions
        return provide_manual_instructions(username)
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 Deployment completed successfully!")
        print("Your Strong No Recoil project is now on GitHub!")
    else:
        print("\n❌ Deployment failed. Please check the instructions above.")
    
    input("\nPress Enter to exit...") 