import os


class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://postgres:231902@localhost/ecotransitiondatabase"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret Key
    SECRET_KEY = os.getenv("SECRET_KEY", "e5b2a5d1f4e3c8d937a6784f1e9c2b3a")

    # Flask-Mail configuration
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # Get from environment variables
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")  # Get from environment variables
    MAIL_DEFAULT_SENDER = os.getenv(
        "MAIL_DEFAULT_SENDER", MAIL_USERNAME
    )  # Use the same email as the sender if not set explicitly
