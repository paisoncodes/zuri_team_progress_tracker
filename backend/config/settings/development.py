from decouple import config
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True

SECRET_KEY = "5467"

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'zuri-progress-tracker.herokuapp.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
