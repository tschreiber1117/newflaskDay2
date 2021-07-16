# import our required packages
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash


# import python modules for our database models

# we'll talk about security in a minute
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# instantiate a database instance
db = SQLAlchemy()

# define a model - results in a database table
# whats happening in the parenthesis in the class line? We're inheriting behavior from a sqlalchemy class -> aka we're telling the computer "hey, this class is a database model"
class Car(db.Model):
    # kind of similar to our CREATE TABLE queries -> we're telling the database what columns/attributes go into this table/model
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=True, default='Unknown')
    year = db.Column(db.Integer, nullable=True, default='Unknown')
    color = db.Column(db.String, nullable=True, default='Unknown')
    miles = db.Column(db.Integer)

    def __repr__(self):
        return f"<Car: {self.name}>"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(254), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def __repr__(self):
        return f"<User: {self.username}>"