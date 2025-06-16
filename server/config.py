import os

# Default to SQLite for development
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL", "sqlite:///app.db"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = True