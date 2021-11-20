#! /bin/bash

source venv/bin/activate

git pull origin deploy

pkill gunicorn

gunicorn --bind localhost:8000 config.wsgi --daemon
