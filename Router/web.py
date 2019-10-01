from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from ..Controller.UserController import UserController

web = Blueprint('app', __name__)
CORS(web)


@web.route('/')
def welcome():
    return jsonify({'result': 'welcome to server'})


@web.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    UserController().create_account(email, password)
    return 'User registered, go to your mailBox and confirm it'


@web.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    return UserController().create_auth_token(email, password)


