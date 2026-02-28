#!/usr/bin/env python3
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set default credentials as environment variables
os.environ.setdefault('SF_USER', 'admin')
os.environ.setdefault('SF_PASS', 'password123')

# Mock argv for SocialFish (empty to trigger env var mode)
sys.argv = ['SocialFish.py']

# Import after setting environment
from core.config import DATABASE
from core.dbsf import initDB
from core.cleanFake import cleanFake

# Initialize database
try:
    cleanFake()
    initDB(DATABASE)
except:
    pass

# Import the Flask app
from SocialFish import app

# Export for Vercel
app = app
