# progress tracker backend



## how to run this project locally
Clone this project

create .env file in the backend directory and add your env variable
```bash
SECRET_KEY= 'it is a secret'
```

create virtual environment
```bash
python -m venv venv
```

activate virtual environment 
```bash
# for windows 
venv\scripts\activate

# for mac 
venv/bin/activate

# for linux
source venv/bin/activate
```

### IMPORTANT: Delete the migrations folder inside the app folder


create a folder name "migrations" inside the "app" folder & also create a "__init__.py" file inside the "migrations" 
```bash
migrations
    __init__.py
```


install dependencies
```bash
pip install -r requirements.txt
```

migrate models
```bash
python manage.py makemigrations

python manage.py migrate
```


run server
```bash
python manage.py runserver
```
