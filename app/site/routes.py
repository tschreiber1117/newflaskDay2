# import whatever modules/functions/classes that we need for our code to work as intended
from flask import Blueprint, render_template, request, flash, redirect, url_for

from flask_login import current_user, login_required

from sqlalchemy.orm import column_property

from werkzeug.security import check_password_hash


# import any database model we're using
from app.models import Car, db

# import our form that we're using
from app.forms import newCarForm, updateCarForm

"""
Note that in the below code, 
some arguments are specified when creating the Blueprint object. 
The first argument, "site", is the Blueprint’s name, 
which is used by Flask’s routing mechanism. 
The second argument, __name__, is the Blueprint’s import name, 
which Flask uses to locate the Blueprint’s resources.
"""
site = Blueprint('site', __name__, template_folder='site_templates')

# each webpage is defined/controlled by a flask route -> which is a python function!

# our homepage route! Hello routing :)
@site.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        username=current_user.username
    else:
        username = "GUEST"
    form = newCarForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            makedata = form.make.data
            modeldata = form.model.data
            yeardata = form.year.data
            colordata = form.color.data
            milesdata = form.miles.data
            
            print(makedata, yeardata)

            # create an animal object in my database based off the form data
            new_car = Car(make=makedata, model=modeldata, year=yeardata, color=colordata, miles=milesdata)

            print("hey")

            #add the newly created animal to our database - always a two step process
            db.session.add(new_car)
            db.session.commit()

            # tell our user that we've added something - using flash messages!
            flash(f'You have successfully added the car {makedata} to your database.')

            return redirect(url_for('site.home'))
    except:
        flash(f'Invalid form input, try again.')
        return redirect(url_for('site.home'))
    return render_template('index.html', form=form, user=username)


# make second route for the profile page
@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@site.route('/cars')
def displayCars():
    a = Car.query.all()
    #car = Car.query.filter
    return render_template('display_cars.html', cars=a)

@site.route('/cars/<int:car_id>')
def individualCar(car_id):
    a = Car.query.get_or_404(car_id)
    return render_template('individual_car.html', car = a)

@site.route('/cars/update/<int:car_id>', methods=["GET", "POST"])
def updateIndividualCar(car_id):
    a = Car.query.get_or_404(car_id)
    updateCar = updateCarForm()
    if request.method == "POST" and updateCar.validate_on_submit():
        modeldata = updateCar.model.data
        yeardata = updateCar.year.data
        colordata = updateCar.color.data
        milesdata = updateCar.miles.data

        a.model = modeldata
        a.year = yeardata
        a.color = colordata
        a.miles = milesdata

        db.session.commit

        flash(f'{a.make} has been updated!')
        return redirect(url_for('site.individualCar', car_id=car_id))

    return render_template('update_individual_car.html', car = a, form=updateCar)

@site.route('/cars/delete/<int:car_id>')
def deleteIndividualCar(car_id):
    a = Car.query.get_or_404(car_id)

    db.session.delete(a)
    db.seesion.commit()

    flash(f"Successfully deleted {a.make}")
    return redirect(url_for('site.displayCars'))

