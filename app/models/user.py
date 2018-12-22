from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Class to define a User in SQLALchemy
class User(UserMixin, db.Model):
    # set the table name as it shows up in the database
    __tablename__='user'

    # init database columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
