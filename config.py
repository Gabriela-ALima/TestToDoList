import os
import random
import string

key = '12356'

class Config:
    DEBUG = False

    database_url = os.getenv("DATABASE_URL")
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = database_url or "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY", key)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", key)