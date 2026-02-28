# COMPRESS APP --------------------------------------------------------------------------------------------------
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
# ---------------------------------------------------------------------------------------------------------------
# LOCAL CONFIGS--------------------------------------------------------------------------------------------------
# Use /tmp for serverless environments like Vercel
import os
if os.environ.get('VERCEL'):
    DATABASE = "/tmp/database.db"
else:
    DATABASE = "./database.db"
url = 'https://github.com/UndeadSec/SocialFish'
red = 'https://github.com/UndeadSec/SocialFish'
sta = 'x'
APP_SECRET_KEY = '<CHANGE ME SF>'
# ---------------------------------------------------------------------------------------------------------------