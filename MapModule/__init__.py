from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "MapModule.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MapModulesecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/MapModule'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Data

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Data.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('MapModule/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
