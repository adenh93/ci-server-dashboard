import os
from .secret import SECRET_KEY, FERNET_KEY

basedir = os.path.abspath(os.path.dirname(__file__))

# Config keys start here
DATABASE_URI = 'sqlite:///app/db/dashboard.db'
SECRET_KEY = SECRET_KEY
FERNET_KEY = FERNET_KEY
ENCODE_ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRY_MINUTES = 30
