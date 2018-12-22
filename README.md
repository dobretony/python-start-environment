# Skeleton for Python Environments
A starting environment for Python3 using virtualenv in order to work.
This is a web server created using Python3 Flask with Bootstrap.

It has the basics utilities for sqlite3, authorization and packages required
to instantly start off creating a web app.

## How to install

First off, you should start with [installing python3 on your machine](https://realpython.com/installing-python/).
With Python3 installed the package virtualenv should already be available.

In order to start the project:

```bash
virtualenv -p python3 venv #creates environment venv inside working directory
source venv/bin/activate #activates venv environment
```

To deactivate the project:

```bash
deactivate
```

When first activating the virtual environment, run:

```bash
make init
```

## Project structure


```bash
README.md # This file.
LICENSE # MIT License
setup.py # Sets up path variables.
requirements.txt # Contains lists of packages for Python
app/__init__.py # initial app entry point
docs/conf.py # configuration for PyDoc
docs/index.md # index file for documentation
tests/test_basic.py # basic tests script
tests/test_advanced.py # advanced tests script
```

## Important links

*[Flask Megatutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
*[Flask Bootstrap How-to](https://pythonhosted.org/Flask-Bootstrap/index.html)

## Timeline:

1. Login and Register views and blueprint
1. SQLite database defined in schema.sql
1. Uses bootstrap/base.html template
1. Has a config.py module in the base package that contains a SECRET_KEY
1. Renamed every template to .j2 so it can be picked up by syntax highlighting
1. Added bootstrap/base.html to base.html.j2
1. login.html.j2 and register.html.j2 now inherit from  base.html.j2
1. Created package 'authorization' that contains the auth.py and forms.py controller and model
1. Added python-wtf and a WTForm for Login
1. Added server side validation for LoginForm in the login method
1. Added flask-sqlalchemy, an ORM for any SQL database
1. Added flask-migrate, a tool for migrating data bases
1. Created migration folder and migration script 
