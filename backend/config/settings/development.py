from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
    "165.22.122.43",
    "progress.zuri.team",
    "zuri-progress-tracker.herokuapp.com",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}