from flask import Flask
from flask_cors import CORS, cross_origin
from .Config import database, auth
from .Router.web import web
from .Router.category import category
from .Router.subcategory import subcategory
from .Router.brand import brand
from .Router.catalog import catalog
from .Router.post import post
from .Router.productOil import productOil
from .Model.UserModel import UserModel
from os import environ
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


def create_app():
    sentry_sdk.init(
        dsn="https://ba181a389d824266889fdb6e8ad7aa80@o384730.ingest.sentry.io/5216416",
        integrations=[FlaskIntegration()]
    )
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['FLASK_APP'] = environ.get('FLASK_APP')
    app.config['FLASK_ENV'] = environ.get('FLASK_ENV')
    app.config['FLASK_DEBUG'] = environ.get('FLASK_DEBUG')
    app.config['UPLOAD_PATH'] = environ.get('UPLOAD_PATH')
    app.config['SERVER_URL'] = environ.get('SERVER_URL')
    app.config['JWT_ACCESS_LIFESPAN'] = {'minutes': 100000}

    app.register_blueprint(web)
    app.register_blueprint(category)
    app.register_blueprint(subcategory)
    app.register_blueprint(brand)
    app.register_blueprint(catalog)
    app.register_blueprint(post)
    app.register_blueprint(productOil)
    # app.before_request_funcs = {
    #     'authenticated': [auth_middleware]
    # }
    database.global_init()
    database.db()
    auth.guard.init_app(app, UserModel)
    return app
