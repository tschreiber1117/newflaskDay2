# if using this, change FLASK_APP in .env to =run.py

from app import app
from app.models import Car, db, User, Car

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Car': Car}