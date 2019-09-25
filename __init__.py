from flask import Flask
from .Config import database, auth
from .Router.web import web
from .Model.UserModel import UserModel
from os import environ


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['JWT_ACCESS_LIFESPAN'] = {'minutes': 100}

    app.register_blueprint(web)
    database.global_init()
    auth.guard.init_app(app, UserModel)
    return app



