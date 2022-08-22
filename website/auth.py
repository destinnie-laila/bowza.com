from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
auth = Blueprint('auth', __name__)

# HTTP methods need to be defined in order to let the route know what 
# it can and cannot do such as collect data which will change the state of the website data or database
# 'POST' method or Retrieve data for a request 'GET' method. These are HTTP methods  

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p> Logout </p>'

@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must contain more than 4 characters.', category="error")
            pass
        elif len(first_name) < 2:
            flash('First Name must contain more than one character.', category="error")
            pass
        elif password1 != password2:
            flash('Passwords must match! Please try again.', category="error")
            pass
        elif len(password1) < 7:
            flash('Password must contain 7 or more characters!', category="error")
            pass
        else:
            new_user = User(email='email', first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()#create new user to db
            flash('Account Created!', category="success")
            return redirect(url_for('views.home'))
            
        
    return render_template('sign_up.html')

