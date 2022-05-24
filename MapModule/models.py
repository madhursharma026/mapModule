from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime, date


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coordinateX = db.Column(db.String(32767), nullable=False)
    coordinateY = db.Column(db.String(32767), nullable=False)
    title = db.Column(db.String(32767), nullable=False)
    description = db.Column(db.String(32767), nullable=False)







