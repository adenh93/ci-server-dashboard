import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Config keys start here
DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'temp/dashboard.db')
