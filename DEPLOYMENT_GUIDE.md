# 🚀 Strong No Recoil - Website Deployment Guide

## 📋 Overview
This guide will help you deploy your Strong No Recoil website to GitHub Pages so it's accessible online.

## 🎯 What You'll Get
- **Live Website**: `https://YOUR_USERNAME.github.io/strong-no-recoil`
- **Download Page**: Clean, professional download interface
- **No Source Code Exposure**: Only shows download options, not the full code

## 🔧 Prerequisites
1. **GitHub Account**: Create one at https://github.com
2. **Git**: Install from https://git-scm.com/
3. **GitHub CLI** (optional): Install from https://cli.github.com/

## 🚀 Quick Deployment (Automated)

### Option 1: Python Script
```bash
python deploy_website.py
```

### Option 2: Batch File
```bash
Double-click: deploy_website.bat
```

## 📋 Manual Deployment Steps

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. **Repository name**: `strong-no-recoil`
3. **Visibility**: Public
4. **Don't** initialize with README
5. Click "Create repository"

### Step 2: Upload Files
1. **Using GitHub Desktop**:
   - Clone the repository
   - Copy all files to the folder
   - Commit and push

2. **Using Git Commands**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/strong-no-recoil.git
   git push -u origin main
   ```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **Deploy from a branch**
5. Select **main** branch
6. Click **Save**

### Step 4: Update Download Links
1. Open `download.js`
2. Replace `YOUR_USERNAME` with your actual GitHub username
3. Commit and push the changes

## 🌐 Your Website URL
Once deployed, your website will be available at:
```
https://YOUR_USERNAME.github.io/strong-no-recoil
```

## 📱 Website Features
- ✅ **Dark Gaming Theme** - Professional design
- ✅ **Download Cards** - Three download options
- ✅ **Feature Showcase** - Highlights app capabilities
- ✅ **Installation Guide** - Step-by-step instructions
- ✅ **Legal Warning** - Important usage notice
- ✅ **Responsive Design** - Works on all devices

## 🔧 Troubleshooting

### 404 Error
- Make sure GitHub Pages is enabled
- Check that files are in the main branch
- Wait 5-10 minutes for deployment

### Download Links Not Working
- Replace `YOUR_USERNAME` in `download.js`
- Make sure repository is public
- Check that files exist in the repository

### Website Not Loading
- Check repository settings
- Verify GitHub Pages is enabled
- Wait for deployment to complete

## 📁 Required Files
```
strong-no-recoil/
├── index.html          # Main website
├── download.js         # Download functionality
├── .github/workflows/pages.yml  # Auto-deployment
├── view_website.py     # Local server
├── deploy_website.py   # Deployment script
└── DEPLOYMENT_GUIDE.md # This guide
```

## 🎉 Success!
Once deployed, users can:
1. Visit your website
2. Choose download option
3. Get installation instructions
4. Download your Strong No Recoil application

## 💡 Tips
- Keep repository public for free hosting
- Update download links when you add new versions
- Test locally before deploying
- Use descriptive commit messages

## 🆘 Need Help?
1. Check GitHub Pages documentation
2. Verify all files are uploaded
3. Ensure repository is public
4. Wait for deployment to complete

Your website will show users exactly how to download your application without exposing all the source code! 