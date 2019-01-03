import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    PROJECT_NAME = "Python Start Environment"
    SECRET_KEY = os.environ.get('PYTHON_START_ENVIRONMENT_SECRET_KEY') or 'O%kC7xe+|lNJFIYvHz%[g*$~d/%7IK+ihQ*zrB2uZ`HGx<d8X:mkv\'H(ugXimGZ'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
