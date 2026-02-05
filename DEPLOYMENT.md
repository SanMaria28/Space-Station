# 🚀 Deploying Space Station to Render

## Step 1: Push to GitHub

1. **Initialize Git repository:**
```powershell
cd "c:\Users\sanma\OneDrive\Desktop\DBMS CIA 3"
git init
git add .
git commit -m "Initial commit - Space Station app"
```

2. **Create GitHub repository:**
   - Go to https://github.com/new
   - Name it: `space-station-command`
   - Don't initialize with README (we already have one)
   - Click "Create repository"

3. **Push to GitHub:**
```powershell
git remote add origin https://github.com/YOUR-USERNAME/space-station-command.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy on Render

1. **Sign up/Login to Render:**
   - Go to https://render.com
   - Sign up with GitHub (recommended)

2. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub account if not already
   - Select the `space-station-command` repository

3. **Configure the service:**
   - **Name**: `space-station` (or any name you like)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python init_sqlite_db.py`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free

4. **Click "Create Web Service"**

5. **Wait for deployment** (usually 2-5 minutes)

## Step 3: Access Your App

Once deployed, Render will provide a URL like:
`https://space-station-XXXX.onrender.com`

**Login with:**
- CrewID: 1, Password: pass101
- CrewID: 2, Password: pass102
- etc.

## Important Notes

⚠️ **Free tier limitations:**
- App sleeps after 15 mins of inactivity
- First request after sleep takes 30-60 seconds
- Database resets on each deploy (use persistent storage for production)

## Troubleshooting

**Build fails?**
- Check logs in Render dashboard
- Ensure all dependencies are in requirements.txt

**App crashes?**
- Check that gunicorn is installed
- Verify database is created during build

**Database issues?**
- Ensure init_sqlite_db.py runs in build command
- Check file permissions

## Updating Your App

```powershell
git add .
git commit -m "Your update message"
git push
```

Render will automatically redeploy!

🌌 Enjoy your space-themed app in the cloud!
