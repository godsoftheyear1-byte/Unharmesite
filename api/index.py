#!/usr/bin/env python3
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set default credentials as environment variables
os.environ.setdefault('SF_USER', 'admin')
os.environ.setdefault('SF_PASS', 'password123')

# Mock argv for SocialFish
sys.argv = ['SocialFish.py', os.environ.get('SF_USER', 'admin'), os.environ.get('SF_PASS', 'password123')]

# Import the Flask app
from SocialFish import app

# Vercel handler
def handler(request, response):
    return app(request, response)

# For local testing
if __name__ == "__main__":
    app.run(debug=True)
