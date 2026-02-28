# SocialFish Setup & Usage Guide

## What is SocialFish?

SocialFish is a phishing education and awareness tool designed for security professionals and penetration testers. It creates fake login pages to demonstrate how phishing attacks work.

⚠️ **IMPORTANT**: This tool is for EDUCATIONAL PURPOSES ONLY. Only use it in authorized security testing environments.

## Installation & Setup

### 1. Install Dependencies

The essential packages have been installed. If you need all features, run:

```bash
pip install -r requirements.txt
```

Core packages installed:
- Flask (web framework)
- Flask-Login (authentication)
- colorama (terminal colors)
- requests (HTTP library)
- qrcode (QR code generation)
- python-nmap (network scanning)
- PyLaTeX (PDF report generation)

### 2. Running SocialFish

Start the application with:

```bash
python SocialFish.py <username> <password>
```

Example:
```bash
python SocialFish.py admin password123
```

The server will start on:
- Local: http://127.0.0.1:5000
- Network: http://0.0.0.0:5000

### 3. Access the Admin Panel

Open your browser and go to:
```
http://127.0.0.1:5000/neptune
```

Login with the credentials you provided when starting the app.

## How to Use SocialFish

### Main Features

1. **Dashboard** (`/creds`)
   - View captured credentials
   - See statistics (attacks, clicks, credentials captured)
   - Monitor phishing campaign effectiveness

2. **Configure Phishing Page** (`/configure`)
   - **Clone Mode**: Clone an existing website (e.g., Facebook, Gmail)
   - **Custom Mode**: Use a custom HTML template
   - Set redirect URL (where victims go after submitting credentials)
   - Optional: Integrate BeEF (Browser Exploitation Framework)

3. **Email Phishing** (`/mail`)
   - Send phishing emails to targets
   - Configure SMTP settings
   - Customize email content and subject

4. **IP Tracing** (`/trace/<ip>`)
   - Geolocate victim IP addresses
   - View location information

5. **Network Scanning** (`/scansf/<ip>`)
   - Scan target networks using Nmap
   - Identify open ports and services

6. **Reports** (`/report`)
   - Generate PDF reports of phishing campaigns
   - Filter by date range, target, company
   - Professional documentation for clients

7. **Manage Professionals & Companies** (`/professionals`, `/companies`)
   - Track security testing clients
   - Organize penetration testing engagements

### Basic Workflow

1. **Start the server**
   ```bash
   python SocialFish.py admin mypassword
   ```

2. **Login to admin panel**
   - Go to http://127.0.0.1:5000/neptune
   - Enter your credentials

3. **Configure a phishing page**
   - Choose "Clone" to copy a real website
   - Enter target URL (e.g., https://facebook.com)
   - Set redirect URL (where to send victims after)
   - Click Configure

4. **Share the phishing link**
   - Your phishing page is at: http://127.0.0.1:5000/
   - Share this with authorized test targets only

5. **Monitor results**
   - View captured credentials in the dashboard
   - Check victim browser info, IP addresses
   - Generate reports for documentation

### Mobile API

SocialFish includes a REST API for mobile control:

- Check API key: `/api/checkKey/<key>`
- Get statistics: `/api/statistics/<key>`
- Get credentials: `/api/getJson/<key>`
- Configure: `/api/configure` (POST)
- Send email: `/api/mail` (POST)
- Trace IP: `/api/trace/<key>/<ip>`
- Scan network: `/api/scansf/<key>/<ip>`

API token is generated automatically and shown in the dashboard.

## Configuration

Edit `core/config.py` to customize:

```python
DATABASE = "./database.db"  # Database location
APP_SECRET_KEY = '<CHANGE ME SF>'  # Change this for security!
```

## Docker Support

Run with Docker:

```bash
docker compose up
```

## Security Notes

1. **Change the secret key** in `core/config.py` before production use
2. **Use HTTPS** in production environments
3. **Restrict access** to the admin panel (/neptune)
4. **Only use** on networks you have permission to test
5. **Document everything** for legal compliance

## Troubleshooting

### Port already in use
If port 5000 is busy, edit `SocialFish.py` line 442:
```python
app.run(host="0.0.0.0", port=5000)  # Change 5000 to another port
```

### Missing dependencies
Install specific packages:
```bash
pip install flask flask-login colorama requests
```

### Database errors
Delete `database.db` and restart to recreate:
```bash
del database.db
python SocialFish.py admin password123
```

## Legal Disclaimer

This tool is for EDUCATIONAL and AUTHORIZED SECURITY TESTING ONLY. Unauthorized use of phishing tools is illegal. Always obtain written permission before testing. The developers assume NO liability for misuse.

## Additional Resources

- Wiki: https://github.com/UndeadSec/SocialFish/wiki
- Setup Guide: https://github.com/UndeadSec/SocialFish/wiki/Setting-Up-SocialFish
- Mobile Controller: https://github.com/UndeadSec/SocialFishMobile

---

**Status**: ✅ Application is running successfully!
**Access**: http://127.0.0.1:5000/neptune
