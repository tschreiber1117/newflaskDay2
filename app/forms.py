# imports for the packages and/or modules we need
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo


class newCarForm(FlaskForm):
    # name, weight, height, climate, region
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    img = StringField('Image URL', validators=[DataRequired()])
    submit_button = SubmitField()

class newUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField()

class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class updateCarForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model')
    year = StringField('Year')
    price = StringField('Price')
    desc = StringField('Description')
    img = StringField('Image URL')
    submit_button = SubmitField()