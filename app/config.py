import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('PYTHON_START_ENVIRONMENT_SECRET_KEY') or 'O%kC7xe+|lNJFIYvHz%[g*$~d/%7IK+ihQ*zrB2uZ`HGx<d8X:mkv\'H(ugXimGZ'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
