# 🚀 Deployment Guide for Space Station Command Center

This guide will help you deploy your Space Station app to Streamlit Cloud for FREE!

## Prerequisites

- A GitHub account (free)
- Your project code ready to push

## Step-by-Step Deployment Instructions

### 1. Push Your Code to GitHub

If you haven't already, create a new repository on GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit your changes
git commit -m "Prepare for deployment"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### 2. Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io
   - Click "Sign in" and use your GitHub account

2. **Create New App**
   - Click "New app" button
   - Select your repository from the dropdown
   - Choose the branch (usually `main` or `master`)
   - Set the main file path to: `app.py`
   - Click "Deploy"!

3. **Wait for Deployment**
   - Streamlit will install dependencies from `requirements.txt`
   - The database will automatically initialize on first run
   - Your app will be live in 2-3 minutes!

### 3. Access Your Deployed App

Once deployed, you'll get a URL like:
```
https://YOUR_USERNAME-space-station-RANDOM.streamlit.app
```

## Sample Login Credentials

Share these with users who want to test your app:

| Role       | Crew ID | Password | Name  |
|------------|---------|----------|-------|
| Commander  | 1       | pass101  | Arjun |
| Pilot      | 2       | pass102  | Lina  |
| Engineer   | 3       | pass103  | Kenji |
| Scientist  | 4       | pass104  | Maria |

## What Changed for Deployment?

✅ **Added auto-database initialization** in `app.py`
   - Database now creates automatically on first run
   - No manual setup needed!

✅ **Created `.streamlit/config.toml`**
   - Custom theme matching your space design
   - Optimized server settings

✅ **Updated `.gitignore`**
   - Excludes database files (they regenerate automatically)
   - Keeps secrets secure

## Troubleshooting

### App won't start?
- Check the logs in Streamlit Cloud dashboard
- Ensure all dependencies are in `requirements.txt`

### Database issues?
- The database auto-initializes on each fresh deployment
- All sample data is included automatically

### Need to update the app?
```bash
git add .
git commit -m "Update app"
git push
```
Streamlit Cloud will automatically redeploy!

## Free Tier Limits

Streamlit Cloud free tier includes:
- ✅ Unlimited public apps
- ✅ 1 GB memory per app
- ✅ Auto-sleep after inactivity (wakes instantly on access)
- ✅ Community support

Perfect for demos and portfolios! 🎉

## Need Help?

- Streamlit Docs: https://docs.streamlit.io
- Community Forum: https://discuss.streamlit.io
- GitHub Issues: Create an issue in your repo

---

**Ready to deploy? Follow the steps above and your app will be live in minutes!** 🚀
