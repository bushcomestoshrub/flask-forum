DEBUG = True
SECRET_KEY = 'secret'

ALLOWED_HOSTS = ['flask-env-one.eba-guz7w6jc.us-west-1.elasticbeanstalk.com']
# flask-assets
# ------------
ASSETS_DEST = 'application/static'


# flask-security
# --------------
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '$2a$10$WyxRXkzAICMHgmqhMGTlJu'
SECURITY_CONFIRMABLE = False
SECURITY_REGISTERABLE = True


# flask-sqlalchemy
# ----------------
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sql'
