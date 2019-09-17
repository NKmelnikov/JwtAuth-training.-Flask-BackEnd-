from flask import Flask, request
from .Config import database
from .Router.web import web


def create_app():
    app = Flask(__name__)
    app.register_blueprint(web)
    database.global_init()
    return app



