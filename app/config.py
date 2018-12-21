import os

class Config(object):
    SECRET_KEY = os.environ.get('PYTHON_START_ENVIRONMENT_SECRET_KEY') or 'O%kC7xe+|lNJFIYvHz%[g*$~d/%7IK+ihQ*zrB2uZ`HGx<d8X:mkv\'H(ugXimGZ'
