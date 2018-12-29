import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from datetime import datetime
from flask_mail import Mail
import logging
from logging.handlers import RotatingFileHandler
import os

# create and configure the new_flask_app
new_flask_app = Flask(__name__, instance_relative_config=True, static_folder='./static')

from app.config import Config
new_flask_app.config.from_object(Config)

if not new_flask_app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/new_python_start_env.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    new_flask_app.logger.addHandler(file_handler)

    new_flask_app.logger.setLevel(logging.INFO)
    new_flask_app.logger.info('Flask application startup')

# ensure the instance folder exists
try:
    os.makedirs(new_flask_app.instance_path)
except OSError:
    pass

mail = Mail(new_flask_app)

# Database Models are defined in the "models" subfolder
# we have to import the db from there
from app.models import db
db.init_app(new_flask_app)
migrate = Migrate(new_flask_app, db)

#activate LoginManager
login = LoginManager(new_flask_app)
login.login_view = 'auth.login'

#set up a user loader function
from app.models.user import User
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# set up before requests
@new_flask_app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

# a simple page that says hello
@new_flask_app.route('/ping')
def hello():
    return 'Hello, World!'

# set the error handlers
import app.views.errors

import app.views.index
#new_flask_app.add_url_rule('/', 'index', index)
#new_flask_app.add_url_rule('/index', 'index', index)
#new_flask_app.add_url_rule('/about', 'about', about)

# register the blueprint for authentication
from app.views.authentication import auth_blueprint
new_flask_app.register_blueprint(auth_blueprint)

#register the blueprint for user profiles
from app.views.settings import settings_blueprint
new_flask_app.register_blueprint(settings_blueprint)
