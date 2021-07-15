# imports for the packages and/or modules we need
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class newCarForm(FlaskForm):
    # name, weight, height, climate, region
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model')
    year = IntegerField('Year')
    color = StringField('Color')
    miles = IntegerField('Miles')
    submit_button = SubmitField()

class newUserForm(FlaskForm):
    username: StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField()

class loginForm(FlaskForm):
    username: StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class updateCarForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model')
    year = IntegerField('Year')
    color = StringField('Color')
    miles = IntegerField('Miles')
    submit_button = SubmitField()