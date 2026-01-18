import random
import string

characters = string.ascii_letters + string.digits + "!@#$%^&*"

key = ''.join(random.choice(characters) for i in range(24))

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = key