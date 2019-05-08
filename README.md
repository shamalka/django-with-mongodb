# Django-with-mongodb
Mongodb database connection to Django and simple get request using Djongo.

Requirements
```
pip install djongo
pip install dnspython
```

Migrate Database
```
python manage.py migrate
```
To Run Server
```
python manage.py runserver
```
Create New Superuser
```
python manage.py createsuperuser
```
MongoDB connection
```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'doc_channel',
        'HOST' : 'mongodb+srv://<username>:<password>@cluster-cghbj.mongodb.net/test?retryWrites=true',
        'USER' : 'username',
        'PASSWORD' : 'password',
    }
}
```
