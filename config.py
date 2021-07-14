  
# imports telling python what outside functions/modules we need in this file

# os module lets us connect .env to this config file
import os

# set the base directory of the project so that we can link files/folder to and from eachother anywhere within the project
basedir = os.path.abspath(os.path.dirname(__file__))

# set up the configuration variables for our flask app
class Config:
    """
        Set config variables for our flask app
        Using environmental variables where necessary
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if os.environ.get('DATABASE_URL').startswith('postgres'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # stop tracking database changes through sqlalchemy