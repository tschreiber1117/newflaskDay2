  
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask.helpers import url_for
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__, template_folder='auth_templates')

from app.forms import newUserForm, loginForm

from app.models import User, db

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = newUserForm()
    if request.method == 'POST' and form.validate_on_submit():
        usernamedata = form.username.data
        emaildata = form.email.data
        passworddata = form.password.data
        
        new_user = User(usernamedata, passworddata, emaildata)

        db.session.add(new_user)
        db.session.commit()

        flash(f'You have successfully signed up with the username : {usernamedata}!')

        return redirect(url_for('auth.signin'))

    return render_template('signup.html', form=form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    f = loginForm()
    if request.method == 'POST' and f.validate_on_submit():
        usernamedata = f.username.data
        passworddata = f.password.data

        user = User.query.filter_by(username=usernamedata).first()
        if user is None or user.password != passworddata:
            flash(f' Incorrect username or password')
            return redirect(url_for('auth.signin'))
        
        login_user(user)
        flash(f'You have successfully signed in! Welcome {usernamedata}')
        return redirect(url_for('site.home'))


    return render_template('signin.html', form = f)

@auth.route('/signout', methods=['GET'])
def signout():
    logout_user()
    return redirect(url_for('site.home'))