import mongoengine
import pymongo
from os import environ


def global_init():
    mongoengine.register_connection(alias='core', name=environ.get('DB_NAME'))
    # mongoengine.connect('todo_list', alias='core')


def db():
    client = pymongo.MongoClient(environ.get('DB_HOST'))
    return client[environ.get('DB_NAME')]
