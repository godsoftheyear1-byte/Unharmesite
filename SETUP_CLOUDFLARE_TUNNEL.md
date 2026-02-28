# 🌐 Share SocialFish Globally with Cloudflare Tunnel

## What is Cloudflare Tunnel?

Cloudflare Tunnel (cloudflared) creates a secure tunnel from your computer to the internet, giving you a public URL like:

```
https://random-name-123.trycloudflare.com
```

Anyone in the world can access this URL!

## 📋 Step-by-Step Setup

### Step 1: Download Cloudflared

**For Windows:**

1. Go to: https://github.com/cloudflare/cloudflared/releases
2. Download: `cloudflared-windows-amd64.exe`
3. Rename it to: `cloudflared.exe`
4. Move it to your SocialFish folder

**Or use this direct download link:**
https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe

### Step 2: Open a NEW Terminal/Command Prompt

Keep your SocialFish server running in the first terminal.

Open a SECOND terminal window.

### Step 3: Navigate to Your SocialFish Folder

```cmd
cd C:\Users\qgee123\SocialFish
```

### Step 4: Run Cloudflared

```cmd
cloudflared tunnel --url http://localhost:5000
```

### Step 5: Get Your Public URL

You'll see output like:

```
+--------------------------------------------------------------------------------------------+
|  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable): |
|  https://random-words-1234.trycloudflare.com                                              |
+--------------------------------------------------------------------------------------------+
```

**Copy that URL!** That's your public phishing link!

## 🎯 How to Use It

### For Victims (Phishing Page):
```
https://your-tunnel-url.trycloudflare.com/
```

### For You (Admin Panel):
```
https://your-tunnel-url.trycloudflare.com/neptune
```

## 📊 Complete Workflow

```
┌─────────────────────────────────────────────────────────┐
│ Terminal 1: SocialFish Server                           │
│ > python SocialFish.py admin password123                │
│ Running on http://127.0.0.1:5000                        │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ Terminal 2: Cloudflare Tunnel                           │
│ > cloudflared tunnel --url http://localhost:5000        │
│ Public URL: https://abc-123.trycloudflare.com           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ Share with victims:                                     │
│ https://abc-123.trycloudflare.com/                     │
│                                                         │
│ Your admin panel:                                       │
│ https://abc-123.trycloudflare.com/neptune              │
└─────────────────────────────────────────────────────────┘
```

## ⚡ Quick Commands

### Windows Command Prompt:
```cmd
# Download cloudflared (run once)
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe -o cloudflared.exe

# Run tunnel
cloudflared.exe tunnel --url http://localhost:5000
```

### PowerShell:
```powershell
# Download cloudflared (run once)
Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile "cloudflared.exe"

# Run tunnel
.\cloudflared.exe tunnel --url http://localhost:5000
```

## 🎨 Configure Your Phishing Page First

Before sharing the link:

1. **Login to dashboard**: https://your-tunnel.trycloudflare.com/neptune
2. **Configure phishing page** (use Custom mode as we discussed)
3. **Test it yourself** first
4. **Then share** the public URL

## 🔒 Security Notes

### Advantages:
✅ Works from anywhere in the world
✅ HTTPS encryption (secure)
✅ No port forwarding needed
✅ No firewall configuration needed
✅ Free to use

### Important:
⚠️ The URL changes each time you restart cloudflared
⚠️ Keep both terminals running (SocialFish + cloudflared)
⚠️ Only share with authorized test participants
⚠️ Document all activities

## 🎯 Alternative: Ngrok

If cloudflared doesn't work, you can also use Ngrok:

### Download Ngrok:
https://ngrok.com/download

### Run Ngrok:
```cmd
ngrok http 5000
```

You'll get a URL like:
```
https://abc123.ngrok.io
```

## 📱 Example Usage Scenario

### Scenario: Testing Employee Awareness

1. **Start SocialFish**:
   ```cmd
   python SocialFish.py admin SecurePass123
   ```

2. **Start Cloudflare Tunnel**:
   ```cmd
   cloudflared tunnel --url http://localhost:5000
   ```

3. **Get public URL**:
   ```
   https://happy-cloud-1234.trycloudflare.com
   ```

4. **Configure phishing page**:
   - Go to: https://happy-cloud-1234.trycloudflare.com/neptune
   - Login and configure Custom mode
   - Set redirect to: https://yourcompany.com

5. **Send to employees**:
   ```
   Subject: Password Reset Required
   
   Dear Employee,
   
   Please reset your password here:
   https://happy-cloud-1234.trycloudflare.com/
   
   IT Department
   ```

6. **Monitor results**:
   - Dashboard: https://happy-cloud-1234.trycloudflare.com/creds
   - See who clicked and who submitted credentials

## 🔧 Troubleshooting

### Problem: "cloudflared: command not found"
**Solution**: Make sure cloudflared.exe is in your current folder or add it to PATH

### Problem: "Connection refused"
**Solution**: Make sure SocialFish is running first on port 5000

### Problem: Tunnel URL not working
**Solution**: Wait 30-60 seconds for the tunnel to become active

### Problem: URL changes every time
**Solution**: This is normal for free tunnels. For permanent URLs, use Cloudflare Zero Trust (requires account)

## 💡 Pro Tips

1. **Use a URL shortener** to make the link look less suspicious:
   - bit.ly
   - tinyurl.com
   - Custom domain

2. **Test the public URL** yourself before sharing

3. **Keep both terminals open** - closing either will stop the service

4. **Monitor in real-time** - refresh the dashboard to see new captures

5. **Document everything** - save the tunnel URL and all activities

## ⚠️ Legal Reminder

Only use this for:
✅ Authorized security testing
✅ Employee awareness training
✅ Educational purposes
✅ With written permission

Never use for:
❌ Unauthorized access
❌ Stealing real credentials
❌ Malicious purposes

---

**Ready to go global!** 🌍
