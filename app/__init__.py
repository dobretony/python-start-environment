import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # register the blueprint for authentication
    from app.authorization import auth
    app.register_blueprint(auth.bp)

    return app
