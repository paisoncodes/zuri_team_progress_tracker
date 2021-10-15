DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'zuri-progress-tracker.herokuapp.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "example",  # production_db,
        "USER": "example",
        "PASSWORD": "example",
        "HOST": "localhost",
        "POST": "",
    }
}
