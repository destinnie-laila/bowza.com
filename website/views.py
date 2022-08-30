from flask import Blueprint, render_template
from flask_login import login_required, current_user
#Blueprint allows us to have multiple views over different pages instead of confined to one page
views = Blueprint('views', __name__)

#creating route, where our users will go to
@views.route('/')
@login_required
#this function will run everytime we activate this route
def home():
    return render_template("home.html")