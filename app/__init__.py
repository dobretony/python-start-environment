import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from datetime import datetime

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_folder='./static')

    from app.config import Config
    app.config.from_object(Config)

    if test_config:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Database Models are defined in the "models" subfolder
    # we have to import the db from there
    from app.models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    # activate Bootstrap
    Bootstrap(app)

    #activate LoginManager
    login = LoginManager(app)
    login.login_view = 'auth.login'

    #set up a user loader function
    from app.models.user import User
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # set up before requests
    @app.before_request
    def before_request():
        if current_user.is_authenticated:
            current_user.last_seen = datetime.utcnow()
            db.session.commit()

    # a simple page that says hello
    @app.route('/ping')
    def hello():
        return 'Hello, World!'

    from app.views.index import index, about
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/about', 'about', about)

    # register the blueprint for authentication
    from app.views.authentication import auth_blueprint
    app.register_blueprint(auth_blueprint)

    #register the blueprint for user profiles
    from app.views.settings import settings_blueprint
    app.register_blueprint(settings_blueprint)

    return app
