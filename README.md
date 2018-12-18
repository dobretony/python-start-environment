# Skeleton for Python Environments
A starting environment for Python3 using virtualenv in order to work.
This is a web server created using Python3 Flask.

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
