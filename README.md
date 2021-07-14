# simple-ecommerce

### for install project

#### DataBase Install:

##### Sqlite

db.sqlite3
#### venv install :

```commandline
$ sudo pip install virtualenv 
$ virtualenv -p /usr/bin/python3.8 venv # path to python interprater python3.
$ source venv/bin/activate
$ pip install -r requirements.txt
```



#### Project Run:

```commandline
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py add_countries # for fill country tabel from country.json 
$ python manage.py createsuperuser # create superuser to use in project
$ python manage.py runserver
```




#### Api Documentation with (Swagger)

http://127.0.0.1:8000/api/doc/swagger/

#### Api Documentation with (ReDoc)

http://127.0.0.1:8000/api/doc/redoc/

#### Api Schema (.json)

http://127.0.0.1:8000/api/doc/schema.json

#### Api Schema (.yaml)

http://127.0.0.1:8000/api/doc/schema.yaml
