import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/dbname")
    SQLALCHEMY_TRACK_MODIFICATIONS = False