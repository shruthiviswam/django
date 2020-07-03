# Django

Django is a high-level Python Web framework that encourages rapid devolopment and clean pragmatic design. A Web framework is a set of components that provide a standard way to devolop websites fast and easy.

There are two main models/architecture used by frameworks :
MVC - Model View Controller
MVT - Model View Template

### Django uses MVT.
#### M - Model indicates databases. Databases are created in models.py. Models are fully class based.
#### V - View connects the database to the framework design. Templates and Models are connected by Views. 
#### T - Template indicates web frameworks. It contains HTML,CSS,JS files to design the output.

## Django Installation & Project Creation:

### Step 1 : 

Download Python

### Step 2 :

Install pip :

```
>sudo apt install python -pip
```

### Step 3 :

Create a folder for Django Project

### Step 4 :

Open terminal in the project folder

### Step 5 :

Create a virtual environment :
Here the name of the virtual environment is "pro"

```
>pip3 install virtualenv
>python -m virtualenv pro
```

### Step 6 :

Activate the virtual environment :

```
(in windows): >pro\Scripts\activate
(in linux): >source pro/bin/activate
```

### Step 7 :

Install Django :

```
>pip3 install django
```

### Step 8 :

Create django proect :
Here the project name is "Project1"

```
>django-admin startproject Project1.
```

### Step 9 :

Run the app :

```
>python manage.py runserver
```

### Step 10 :

Go to the localhost : 
This is seen.

```
"Django install worked successfully!"
```

### Step 11 :

Make migrations : 

```
>python manage.py makemigrations
>python manage.py migrate
```

### Step 12 :

Run the app :

```
>python manage.py runserver
```


## Structure of Django :

The initial project structure is composed of five files. 

### manage.py : 
Its a shortcut to use the django-admin command line utility. Its used to run management commands related to the project. It will be used to run the devolopment server, run tests, create migrations and much more.

### __init__.py : 
This empty file tells Python that its a Python Package.

### settings.py : 
It contains all the project's configuration. To add any new features, this is the file to make changes first.

### urls.py:
Its responsible for mapping the routes and paths in the project. 

### wsgi.py:
Its a simple geteway interface used for deployment.
