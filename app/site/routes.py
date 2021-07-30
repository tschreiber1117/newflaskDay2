# import whatever modules/functions/classes that we need for our code to work as intended
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

from flask_login import current_user, login_required

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
            pricedata = form.price.data
            descdata = form.desc.data
            imgdata = form.img.data

            print(makedata)

            # create an animal object in my database based off the form data
            new_car = Car(make=makedata, model=modeldata, year=yeardata, price=pricedata, desc=descdata, img=imgdata)

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
@login_required
def updateIndividualCar(car_id):
    a = Car.query.get_or_404(car_id)
    updateCar = updateCarForm()
    if request.method == "POST" and updateCar.validate_on_submit():
        makedata = updateCar.make.data
        modeldata = updateCar.model.data
        yeardata = updateCar.year.data
        pricedata = updateCar.price.data
        descdata = updateCar.desc.data
        imgdata = updateCar.img.data

        # deal with price being a string and needing conversion
        if updateCar.price.data:
            try:
                a.price = float(updateCar.price.data)
                print('changed price')
            except:
                flash(f"Invalid Price, couldn't update.")
                return redirect(url_for('site.individualCar', car_id=car_id))
        print('got past form data')
        #fixed update to actually update thee car if data present from the form
        if makedata:
            a.make = makedata
            print('changed make')
        if modeldata:
            a.model = modeldata
            print('changed model')
        if yeardata:
            a.year = yeardata
            print('changed year')
        if descdata:
            a.desc = descdata
            print('changed desc')
        if imgdata:
            a.img = imgdata
            print('changed img')

        print(makedata, modeldata, descdata, updateCar.price.data)

        db.session.commit

        flash(f'{a.make} has been updated!')
        return redirect(url_for('site.individualCar', car_id=car_id))

    return render_template('update_individual_car.html', car = a, form=updateCar)

@site.route('/cars/delete/<int:car_id>')
def deleteIndividualCar(car_id):
    a = Car.query.get_or_404(car_id)

    db.session.delete(a)
    db.session.commit()

    flash(f"Successfully deleted {a.make}")
    return redirect(url_for('site.displayCars'))

# Add a Public API endpoint that anyone can access to get my product information
# Note: be careful about using public API endpoints -> we can talk about authentication required api endpoints another day
# a public api endpoint can lead to unintentionally large cloud hosting costs if not set up properly
# this is a simplified and improper implementation below
@site.route('/products', methods=['GET'])
def get_products():
    """
    [GET] /products returns jsonified data on the animals within our database
    """
    # query database to get the animals
    cars = Car.query.all()
    print(cars)
    # turn the list of animal objects into a list of animal dictionaries
    cars = [car.to_dict() for car in cars]
    # jsonify that list
    cars = jsonify(cars)
    # return that list
    return cars