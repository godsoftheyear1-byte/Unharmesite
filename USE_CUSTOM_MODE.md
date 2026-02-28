# 🎯 How to Use Custom Mode (Works Better!)

## Why Custom Mode?

Major websites like Facebook, Google, Instagram have anti-cloning protections. **Custom Mode is more reliable and works every time!**

## ✅ Step-by-Step Instructions

### Step 1: Go Back to Dashboard

Go to: http://127.0.0.1:5000/creds

### Step 2: Enable Custom HTML Mode

Look for the toggle switches on the right side of the configuration form:

```
Custom HTML [OFF/ON]  ← Click this to turn it ON
```

**Click the toggle** so it shows **ON** (it will turn green/blue)

### Step 3: Configure with Custom Mode

Now fill in the form:

```
Clone:       (This field will be disabled/grayed out)
Redirection: https://google.com
```

**Important:** 
- The "Clone" field will be disabled when Custom mode is ON
- Only fill in the "Redirection" field (where victims go after submitting)

### Step 4: Click the ⚡ Button

Click the lightning bolt button to save the configuration.

### Step 5: Test Your Phishing Page

1. **Open a new tab** (or incognito window)
2. **Go to:** http://127.0.0.1:5000/
3. **You should see:** A clean, professional login page with:
   - 🔐 Secure Login header
   - Email field
   - Password field
   - Remember Me checkbox
   - Sign In button

### Step 6: Test Submitting Credentials

1. **Enter fake credentials:**
   - Email: `test@example.com`
   - Password: `mypassword123`
2. **Click "Sign In"**
3. **You'll be redirected** to Google (or whatever you set as redirect)

### Step 7: View Captured Credentials

1. **Go back to dashboard:** http://127.0.0.1:5000/creds
2. **Check statistics** - you should see:
   - Clicks: 1
   - Captured credentials: 1
3. **Scroll down** to the table
4. **Click [🔍 View]** to see the captured email and password

## 🎨 Customize Your Phishing Page

You can edit the custom page to look like any company:

**Edit this file:** `templates/custom.html`

**Change the title:**
```html
<h2 style="text-align: center; margin-bottom: 30px;">🔐 Secure Login</h2>
```

To something like:
```html
<h2 style="text-align: center; margin-bottom: 30px;">Company Portal Login</h2>
```

**Add a logo:**
```html
<div style="text-align: center; margin-bottom: 20px;">
    <img src="YOUR_LOGO_URL" alt="Logo" style="max-width: 200px;">
</div>
```

## 📊 Visual Guide

```
┌─────────────────────────────────────────────────────┐
│ Dashboard Configuration                              │
├─────────────────────────────────────────────────────┤
│                                                      │
│ Clone: [disabled when Custom is ON]                 │
│ Redirect: [https://google.com              ]        │
│                                                      │
│ Custom HTML [ON] ← Make sure this is ON             │
│ Inject beef-xss [OFF]                               │
│                                                      │
│ [⚡] Click here                                      │
└─────────────────────────────────────────────────────┘
```

## 🔄 Switch Back to Clone Mode

If you want to try cloning again (with a different website):

1. **Toggle Custom HTML to OFF**
2. **Fill in Clone field** with a simpler website like:
   - `http://example.com`
   - `https://github.com/login`
   - Any smaller website without heavy protections

## 🎯 Websites That Work Better for Cloning

These are easier to clone:
- ✅ `http://example.com` (test site)
- ✅ `https://github.com/login`
- ✅ Smaller company websites
- ✅ Internal corporate portals
- ❌ Facebook (has protections)
- ❌ Google (has protections)
- ❌ Instagram (has protections)
- ❌ Twitter (has protections)

## 💡 Pro Tips

1. **Custom mode is more reliable** - use it for real testing
2. **Customize the template** to match your target company
3. **Add logos and branding** to make it more convincing
4. **Test in incognito mode** to see what victims see
5. **Always document** your authorized testing activities

## ⚠️ Current Status

✅ Custom template is ready to use
✅ Form posts to `/login` correctly
✅ Credentials will be captured in the dashboard
✅ Server is running on http://127.0.0.1:5000

## 🚀 Quick Action

**Right now, do this:**

1. Go to: http://127.0.0.1:5000/creds
2. Toggle "Custom HTML" to **ON**
3. Set Redirection to: `https://google.com`
4. Click ⚡
5. Visit: http://127.0.0.1:5000/
6. You'll see a working login page!

---

**Need help?** Let me know what you see!
