#! /bin/bash

cd ..

git stash

git pull origin deploy

source venv/bin/activate

pip3 install -r requirements.txt --upgrade

cd /frontend

yarn install

yarn build

cd ../backend

# python3 manage.py collectstatic --noinput

fuser -k 8000/tcp

gunicorn --bind localhost:8000 config.wsgi --daemon
