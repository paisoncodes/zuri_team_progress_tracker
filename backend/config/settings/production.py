import os,dj_database_url,subprocess


DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'zuri-progress-tracker.herokuapp.com']

bashCommand = "heroku config:get DATABASE_URL -a zuri-progress-tracker" #Use your app_name

# output = subprocess.check_output(["bash",'-c', bashCommand]).decode("utf-8")
DATABASES['default'] = dj_database_url.config(default='postgres://cxikigeralbxbt:89d6e5293ed885752368ed73b0d49bf0e7625c97b063725bff13f62ee68ed74f@ec2-34-197-182-7.compute-1.amazonaws.com:5432/d1hv492c8vls4e',conn_max_age=600, ssl_require=True)
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
