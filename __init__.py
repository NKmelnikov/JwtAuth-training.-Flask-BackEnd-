from flask import Flask
from .Config import database, auth
from .Router.web import web
from .Router.authenticated import authenticated, auth_middleware
from .Model.UserModel import UserModel
from os import environ


def create_app():
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['FLASK_APP'] = environ.get('FLASK_APP')
    app.config['FLASK_ENV'] = environ.get('FLASK_ENV')
    app.config['JWT_ACCESS_LIFESPAN'] = {'minutes': 1}

    app.register_blueprint(web)
    app.register_blueprint(authenticated)
    app.before_request_funcs = {
        'authenticated': [auth_middleware]
    }
    database.global_init()
    auth.guard.init_app(app, UserModel)
    return app
