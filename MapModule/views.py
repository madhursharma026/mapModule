from flask import Blueprint, render_template, request, flash, redirect, url_for, json
from flask_login import login_required, current_user, logout_user
from numpy import tile
from sqlalchemy import func
from . import db
from .models import Data

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template('homepage.html')


@views.route('/save_data_to_mysql/<coordinateX>/<coordinateY>/<title>/<description>')
def api_get_name(coordinateX, coordinateY, title, description):
    new_data = Data(coordinateX=coordinateX, coordinateY=coordinateY, title=title, description=description)
    db.session.add(new_data)
    db.session.commit()
    return redirect(url_for('views.home'))



# @views.route('/save_data_to_mysql/', methods=['POST'])
# def api_get_name():
#     coordinateX = request.json.coordinateX
#     coordinateY = request.json.coordinateY
#     title = request.json.title
#     description = request.json.description
#     new_data = Data(coordinateX=coordinateX, coordinateY=coordinateY, title=title, description=description)
#     db.session.add(new_data)
#     db.session.commit()
#     return render_template('a.html', coordinateX=coordinateX, coordinateY=coordinateY, title=title, description=description)