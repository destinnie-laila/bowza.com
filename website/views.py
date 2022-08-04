from flask import Blueprint, render_template
#Blueprint allows us to have multiple views over different pages instead of confined to one page
views = Blueprint('views', __name__)

#creating route, where our users will go to
@views.route('/')
#this function will run everytime we activate this route
def home():
    return render_template("home.html")