from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

# HTTP methods need to be defined in order to let the route know what 
# it can and cannot do such as collect data which will change the state of the website data or database
# 'POST' method or Retrieve data for a request 'GET' method. These are HTTP methods  

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', text="testing")

@auth.route('/logout')
def logout():
    return '<p> Logout </p>'

@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')

