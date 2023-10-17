from flask import Blueprint, redirect, render_template, request, url_for

from . import db
from .models import Destination

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()    
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Destination).where(Destination.name.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
