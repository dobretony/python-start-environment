from . import db

# Class to define a User in SQLALchemy
class User(db.Model):
    # set the table name as it shows up in the database
    __tablename__='user'

    # init database columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
