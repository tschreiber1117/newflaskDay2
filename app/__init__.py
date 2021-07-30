# import necessary packages/modules (in this case the Flask class and Config class)
from flask import Flask
from config import Config

# import our Blueprint object from the blueprint's routes file
from .site.routes import site
from .authentication.routes import auth
from .payments.routes import payments

# import our database stuff
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db, login
from flask_cors import CORS

# import login authentification



# define our application as instance of the Flask object
app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:3000'])

# register our blueprints
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(payments)

# configure our application based on the Config class from the config.py file
app.config.from_object(Config)

#configure our database
db.init_app(app)

migrate = Migrate(app, db)

# configure login manager
login.init_app(app)
login.login_view = 'auth.signin'
login.login_message_category = 'danger'


# bring in our models (importing the models.py file)
from . import models