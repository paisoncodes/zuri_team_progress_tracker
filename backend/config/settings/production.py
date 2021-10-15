import os,dj_database_url


DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'zuri-progress-tracker.herokuapp.com']


DATABASES[‘default’] = dj_database_url.config(default=output,conn_max_age=600, ssl_require=True)
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "example",  # production_db,
#         "USER": "example",
#         "PASSWORD": "example",
#         "HOST": "localhost",
#         "POST": "",
#     }
# }
