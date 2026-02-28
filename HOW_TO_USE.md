# SocialFish - Step-by-Step Usage Guide

## Step 1: Start the Application

Open your terminal and run:

```bash
python SocialFish.py admin password123
```

You should see:
```
███████ ████████ ███████ ██ ███████ ██       ███████ ██ ███████ ██   ██ 
Go to http://0.0.0.0:5000/neptune to start
* Running on http://127.0.0.1:5000
```

## Step 2: Access the Admin Panel

1. Open your web browser
2. Go to: **http://127.0.0.1:5000/neptune**
3. You'll see a login page

**Login credentials:**
- Email/Username: `admin`
- Password: `password123`

## Step 3: Configure a Phishing Page

Once logged in, you'll see the dashboard. Here's how to set up a phishing page:

### Option A: Clone an Existing Website (Recommended)

1. **In the dashboard**, look for the configuration form
2. **Fill in the fields**:

   ```
   Target URL: https://facebook.com
   (The website you want to clone)
   
   Redirect URL: https://facebook.com
   (Where victims go after submitting credentials)
   
   Status: Clone
   (Select "Clone" mode)
   
   BeEF Hook: (leave empty unless using BeEF)
   ```

3. **Click "Configure" or "Submit"**

4. **Your phishing page is now live at**: http://127.0.0.1:5000/

### Option B: Use Custom HTML Template

1. **Create your custom HTML** in `templates/custom.html`
2. **Important**: Your form must POST to `/login`

Example custom form:
```html
<form method="POST" action="/login">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Login</button>
</form>
```

3. **In the dashboard configuration**:
   ```
   Status: Custom
   Redirect URL: https://example.com
   ```

4. **Click "Configure"**

## Step 4: Test Your Phishing Page

1. **Open a new browser tab** (or incognito window)
2. **Go to**: http://127.0.0.1:5000/
3. **You should see**: The cloned website or your custom page
4. **Try submitting fake credentials** to test

## Step 5: Monitor Captured Credentials

### View in Dashboard

1. **Go back to**: http://127.0.0.1:5000/neptune
2. **Login** if needed
3. **You'll see the main dashboard** with:

   - **Total Attacks**: Number of phishing campaigns configured
   - **Total Clicks**: Number of visitors to your phishing page
   - **Credentials Captured**: Number of successful credential captures
   - **Not Picked Up**: Visitors who didn't submit credentials

### View Detailed Credentials

In the dashboard, you'll see a table with captured data:

| ID | URL | Date | Browser | Version | Platform | IP Address | Actions |
|----|-----|------|---------|---------|----------|------------|---------|
| 1 | facebook.com | 02-28-2026 | Chrome | 120.0 | Windows | 192.168.1.100 | View Details |

**Click "View Details"** on any entry to see:
- Complete form data submitted (username, password, etc.)
- Full JSON of captured information
- Timestamp and user agent details

### View Individual Credential Details

1. **Click on an ID number** or "View" button
2. **You'll see**: http://127.0.0.1:5000/single/1
3. **This shows**: All form fields submitted by the victim in JSON format

Example:
```json
{
  "username": "testuser@email.com",
  "password": "testpass123",
  "remember": "on"
}
```

## Step 6: Additional Features

### Trace IP Address

1. **In the credentials table**, click on an IP address
2. **Or go to**: http://127.0.0.1:5000/trace/192.168.1.100
3. **You'll see**:
   - Country, City, Region
   - ISP information
   - Coordinates
   - Timezone

### Scan Network

1. **Click "Scan"** next to an IP address
2. **Or go to**: http://127.0.0.1:5000/scansf/192.168.1.100
3. **You'll see**: Open ports and services (requires nmap installed)

### Send Phishing Emails

1. **Go to**: http://127.0.0.1:5000/mail
2. **Configure SMTP settings**:
   ```
   Email: your-email@gmail.com
   Password: your-app-password
   SMTP Server: smtp.gmail.com
   Port: 587
   ```

3. **Compose email**:
   ```
   Subject: Password Reset Required
   Recipient: target@example.com
   Body: Click here to reset: http://127.0.0.1:5000/
   ```

4. **Click "Send"**

### Generate Reports

1. **Go to**: http://127.0.0.1:5000/report
2. **Select filters**:
   - Date range
   - Target URL
   - Professional/Company
3. **Click "Generate Report"**
4. **Download PDF** with all captured data

## Real-World Example Workflow

### Scenario: Testing Employee Awareness

1. **Start SocialFish**:
   ```bash
   python SocialFish.py admin SecurePass123
   ```

2. **Configure to clone Office 365**:
   - Target URL: `https://login.microsoftonline.com`
   - Redirect URL: `https://office.com`
   - Status: Clone

3. **Share the link** with authorized test participants:
   - http://YOUR-IP:5000/

4. **Monitor the dashboard** to see:
   - Who clicked the link
   - Who submitted credentials
   - What credentials they used

5. **Generate a report** for management showing:
   - Success rate of phishing attempt
   - Employee awareness levels
   - Recommendations for training

## Important Notes

### Database Location

All captured data is stored in: `./database.db`

You can view it with:
```bash
sqlite3 database.db
SELECT * FROM creds;
```

### Reset Everything

To start fresh:
```bash
del database.db
python SocialFish.py admin password123
```

### Change Admin Credentials

Edit the command when starting:
```bash
python SocialFish.py myusername mypassword
```

### Access from Other Devices

If you want to access from other computers on your network:

1. **Find your IP address**:
   ```bash
   ipconfig  # Windows
   ```

2. **Share this URL**: http://YOUR-IP:5000/

3. **Admin panel**: http://YOUR-IP:5000/neptune

### Mobile API Access

Get your API token from the dashboard, then use:

```bash
# Check statistics
curl http://127.0.0.1:5000/api/statistics/YOUR-TOKEN

# Get all credentials
curl http://127.0.0.1:5000/api/getJson/YOUR-TOKEN
```

## Troubleshooting

### "Page not found" when accessing phishing page

**Solution**: Make sure you configured a phishing page first in the dashboard

### Credentials not showing up

**Solution**: 
1. Check that your form POSTs to `/login`
2. Verify the database exists: `dir database.db`
3. Check browser console for errors

### Can't access from other devices

**Solution**:
1. Check firewall settings
2. Make sure you're using your actual IP, not 127.0.0.1
3. Ensure port 5000 is open

### Clone mode not working

**Solution**:
1. Target website might block cloning
2. Try a different website
3. Use Custom mode instead

## Security Reminders

⚠️ **CRITICAL**:
- Only use on networks you own or have written permission to test
- Document all testing activities
- Inform participants this is a security test
- Never use for malicious purposes
- Follow all local laws and regulations

## Quick Reference

| Action | URL |
|--------|-----|
| Admin Login | http://127.0.0.1:5000/neptune |
| Phishing Page | http://127.0.0.1:5000/ |
| Dashboard | http://127.0.0.1:5000/creds |
| Send Email | http://127.0.0.1:5000/mail |
| Reports | http://127.0.0.1:5000/report |
| View Credential | http://127.0.0.1:5000/single/ID |
| Trace IP | http://127.0.0.1:5000/trace/IP |
| Scan Network | http://127.0.0.1:5000/scansf/IP |

---

**You're all set!** Start by accessing http://127.0.0.1:5000/neptune and logging in.
