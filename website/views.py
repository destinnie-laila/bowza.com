from crypt import methods
from unicodedata import category
from urllib import request
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Note

#Blueprint allows us to have multiple views over different pages instead of confined to one page
views = Blueprint('views', __name__)

#creating route, where our users will go to
@views.route('/', methods=['GET', 'POST'])
@login_required
#this function will run everytime we activate this route
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note has no content!', category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.sessions.add(new_note)
            db.sessions.commit()
            flash('Note has been added!' category="success")
            
    return render_template("home.html", user=current_user)