from flask import Blueprint
#Blueprint allows us to have multiple views over different pages instead of confined to one page
views = Blueprint('views', __name__)

#creating route, where our users will go to
@views.route('/')
def home():
    return "<h1>Test</h1>"