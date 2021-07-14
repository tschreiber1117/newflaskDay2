# imports for the packages and/or modules we need
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class newCarForm(FlaskForm):
    # name, weight, height, climate, region
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model')
    year = IntegerField('Year')
    color = StringField('Color')
    miles = IntegerField('Miles')
    submit_button = SubmitField()