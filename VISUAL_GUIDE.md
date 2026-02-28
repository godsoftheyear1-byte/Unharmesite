# SocialFish Visual Interface Guide

## 🎯 Dashboard Overview

When you login at http://127.0.0.1:5000/neptune, you'll see this layout:

```
┌─────────────────────────────────────────────────────────────────┐
│  🐟 SocialFish                                                   │
│  Your attacks url: http://0.0.0.0:5000                          │
│                                                                  │
│  [Clone URL Input] [Redirect URL Input] [⚡ Submit Button]      │
│                                                                  │
│  Custom HTML [OFF/ON]  Inject beef-xss [OFF/ON]                │
└─────────────────────────────────────────────────────────────────┘
```

## 📝 Step-by-Step: Configure Phishing Page

### Configuration Form Fields:

```
┌──────────────────────────────────────────────────────────┐
│ Clone:       [https://facebook.com                    ] │
│              ↑ Enter the website you want to clone       │
│                                                          │
│ Redirection: [https://facebook.com                    ] │
│              ↑ Where victims go after submitting        │
│                                                          │
│              [⚡] ← Click to configure                   │
└──────────────────────────────────────────────────────────┘
```

### Example Configurations:

#### 1. Clone Facebook Login
```
Clone:       https://facebook.com
Redirection: https://facebook.com
Custom HTML: OFF
Beef-XSS:    OFF
```

#### 2. Clone Gmail Login
```
Clone:       https://accounts.google.com
Redirection: https://mail.google.com
Custom HTML: OFF
Beef-XSS:    OFF
```

#### 3. Use Custom HTML Template
```
Clone:       (disabled when Custom is ON)
Redirection: https://example.com
Custom HTML: ON  ← Toggle this switch
Beef-XSS:    OFF
```

## 📊 Dashboard Statistics

After configuration, you'll see 4 stat boxes:

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   🖱️ 25     │  │   😞 15     │  │   📋 10     │  │   🔥 3      │
│   clicks    │  │  visitors   │  │  captured   │  │  attacks    │
│             │  │ not picked  │  │ credentials │  │  launched   │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
```

**What these mean:**
- **Clicks**: Total visitors to your phishing page
- **Visitors not picked up**: People who visited but didn't submit credentials
- **Captured credentials**: Successful phishing attempts
- **Attacks launched**: Number of times you configured a phishing page

## 📋 Credentials Table

Below the stats, you'll see captured credentials:

```
┌──────────────────────────────────────────────────────────────────────────┐
│ Successful attacks                                                        │
├──────────┬──────────────┬──────────┬──────────┬──────────┬──────────────┤
│ URL      │ IP           │ Browser  │ OS       │ Date     │ Actions      │
├──────────┼──────────────┼──────────┼──────────┼──────────┼──────────────┤
│ facebook │ 192.168.1.10 │ Chrome   │ Windows  │ 02-28-26 │ [TRACE]      │
│ .com     │ [👁️ TRACE]   │ v120     │          │          │ [🎯 Scan]    │
│          │              │          │          │          │ [🕷️ Shodan]  │
│          │              │          │          │          │ [🔍 View]    │
├──────────┼──────────────┼──────────┼──────────┼──────────┼──────────────┤
│ gmail    │ 192.168.1.25 │ Firefox  │ Linux    │ 02-27-26 │ [TRACE]      │
│ .com     │ [👁️ TRACE]   │ v115     │          │          │ [🎯 Scan]    │
│          │              │          │          │          │ [🕷️ Shodan]  │
│          │              │          │          │          │ [🔍 View]    │
└──────────┴──────────────┴──────────┴──────────┴──────────┴──────────────┘
```

### Action Buttons Explained:

1. **👁️ TRACE** - Shows geolocation of the IP address
2. **🎯 Scan** - Runs nmap port scan on the IP
3. **🕷️ Shodan** - Opens Shodan.io for the IP (external site)
4. **🔍 View** - Shows the actual credentials submitted

## 🔍 Viewing Captured Credentials

Click **[🔍 View]** to see the actual data:

```
┌─────────────────────────────────────────────────────┐
│ Credential Details - ID: 1                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│ {                                                   │
│   "email": "victim@example.com",                    │
│   "password": "password123",                        │
│   "remember": "on"                                  │
│ }                                                   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## 🌍 IP Tracing

Click **[👁️ TRACE]** to see location:

```
┌─────────────────────────────────────────────────────┐
│ IP Trace: 192.168.1.10                              │
├─────────────────────────────────────────────────────┤
│ Country:    United States                           │
│ Region:     California                              │
│ City:       San Francisco                           │
│ ISP:        Comcast Cable                           │
│ Latitude:   37.7749                                 │
│ Longitude:  -122.4194                               │
│ Timezone:   America/Los_Angeles                     │
└─────────────────────────────────────────────────────┘
```

## 🎯 Network Scanning

Click **[🎯 Scan]** to see open ports:

```
┌─────────────────────────────────────────────────────┐
│ Nmap Scan: 192.168.1.10                             │
├─────────────────────────────────────────────────────┤
│ Port 22:   SSH (Open)                               │
│ Port 80:   HTTP (Open)                              │
│ Port 443:  HTTPS (Open)                             │
│ Port 3306: MySQL (Filtered)                         │
└─────────────────────────────────────────────────────┘
```

## 📧 Sending Phishing Emails

Click **[📧 Send Mail]** button in the dashboard:

```
┌─────────────────────────────────────────────────────┐
│ Send Phishing Email                                 │
├─────────────────────────────────────────────────────┤
│ Your Email:    [your-email@gmail.com            ]  │
│ Password:      [••••••••••••••••                ]  │
│ SMTP Server:   [smtp.gmail.com                  ]  │
│ Port:          [587                             ]  │
│                                                     │
│ Recipient:     [target@example.com              ]  │
│ Subject:       [Password Reset Required         ]  │
│ Body:          [                                ]  │
│                [Click here to reset your pass   ]  │
│                [http://YOUR-IP:5000/            ]  │
│                                                     │
│                [Send Email]                         │
└─────────────────────────────────────────────────────┘
```

### Gmail SMTP Settings:
```
SMTP Server: smtp.gmail.com
Port: 587
Email: your-email@gmail.com
Password: Use "App Password" not regular password
```

**How to get Gmail App Password:**
1. Go to Google Account settings
2. Security → 2-Step Verification
3. App passwords → Generate new
4. Use that password in SocialFish

## 📄 Generate Reports

Click **[📄 Generate Report]** button:

```
┌─────────────────────────────────────────────────────┐
│ Generate Phishing Report                            │
├─────────────────────────────────────────────────────┤
│ Report Title:  [Employee Awareness Test          ] │
│                                                     │
│ Date Range:    [02/01/2026 - 02/28/2026         ] │
│                                                     │
│ Target URL:    [All ▼]                             │
│                - All                                │
│                - facebook.com                       │
│                - gmail.com                          │
│                                                     │
│ Professional:  [Select ▼]                          │
│ Company:       [Select ▼]                          │
│                                                     │
│                [Generate PDF Report]                │
└─────────────────────────────────────────────────────┘
```

## 🔐 API Token & Mobile Access

In the dashboard, you'll see:

```
┌─────────────────────────────────────────────────────┐
│ Easy Access                                         │
│                                                     │
│  [QR CODE]  ← Scan with mobile app                 │
│                                                     │
│  Your App Token: abc123xyz789def456                │
│  [🔄 Revoke Token]                                  │
│                                                     │
│  📱 Control SocialFish via mobile app               │
└─────────────────────────────────────────────────────┘
```

## 🎬 Complete Workflow Example

### Scenario: Test Facebook Phishing

**1. Start the server:**
```bash
python SocialFish.py admin mypassword
```

**2. Login:**
- Open: http://127.0.0.1:5000/neptune
- Enter: admin / mypassword

**3. Configure:**
```
Clone:       https://facebook.com
Redirection: https://facebook.com
[Click ⚡ button]
```

**4. Share phishing link:**
```
Send to test target: http://YOUR-IP:5000/
```

**5. Monitor dashboard:**
- Watch "clicks" increase when someone visits
- Watch "captured credentials" when someone submits

**6. View details:**
- Click [🔍 View] to see username/password
- Click [👁️ TRACE] to see location
- Click [🎯 Scan] to scan their network

**7. Generate report:**
- Click [📄 Generate Report]
- Select date range
- Download PDF

## 🚨 Important URLs Reference

```
┌──────────────────────────────────────────────────────┐
│ Purpose              │ URL                           │
├──────────────────────┼───────────────────────────────┤
│ Admin Login          │ /neptune                      │
│ Dashboard            │ /creds                        │
│ Phishing Page        │ /                             │
│ Send Email           │ /mail                         │
│ Generate Report      │ /report                       │
│ View Credential      │ /single/1                     │
│ Trace IP             │ /trace/192.168.1.10           │
│ Scan Network         │ /scansf/192.168.1.10          │
│ Manage Professionals │ /professionals                │
│ Manage Companies     │ /companies                    │
└──────────────────────┴───────────────────────────────┘
```

## 💡 Pro Tips

1. **Test first**: Always test with your own credentials before deploying
2. **Use incognito**: Test the phishing page in incognito mode
3. **Check database**: View `database.db` to verify data is being captured
4. **Network access**: Use your actual IP (not 127.0.0.1) for network access
5. **Firewall**: Make sure port 5000 is open in your firewall

## 🔧 Troubleshooting Visual Guide

### Problem: Can't see configuration form
```
✗ Not logged in → Go to /neptune and login
✓ Logged in → You should see the form at top of dashboard
```

### Problem: Credentials not appearing
```
✗ Form not posting to /login → Check your HTML form action
✓ Form posts to /login → Check database: sqlite3 database.db
```

### Problem: Clone not working
```
✗ Website blocks cloning → Try different site or use Custom mode
✓ Clone successful → Phishing page appears at http://127.0.0.1:5000/
```

---

**You're ready to use SocialFish!** 🎣

Start at: http://127.0.0.1:5000/neptune
