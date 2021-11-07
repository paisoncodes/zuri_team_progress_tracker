import os, dj_database_url, subprocess
from decouple import config

DEBUG = False
SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
    "165.22.122.43",
    "progress.zuri.team",
    "zuri-progress-tracker.herokuapp.com",
]

bashCommand = (
    "heroku config:get DATABASE_URL -a zuri-progress-tracker"  # Use your app_name
)

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
