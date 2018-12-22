from flask_sqlalchemy import SQLAlchemy

# create a Database object here in order to load all the models in this package
# init_app() will be called in the create_app() part of the main package in order
# to initialize the database and integrate it into the Flask app
db = SQLAlchemy()

# Helper function to load all the models
def load_models():
    from app.models.user import User
    from app.models.comment import Comment
    print("Loaded Models")

# Run helper function on load in order for it to be picked up by flask-migrate
load_models()
