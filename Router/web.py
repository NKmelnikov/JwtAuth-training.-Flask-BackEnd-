from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.UserController import UserController
from ..Controller.PostController import PostController
from ..Helper.UploadHelper import UploadHelper

web = Blueprint('app', __name__)
CORS(web, resources={r"/*": {"origins": "*"}})


@web.route('/')
def welcome():
    return jsonify({'response': 'welcome to server'})


@web.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    UserController().create_account(email, password)
    return jsonify({'response': 'Ok'})


@web.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    return UserController().create_auth_token(email, password)


@web.route('/upload-file', methods=['POST'])
def upload_file():
    json_data = request.get_json()
    return UploadHelper().upload_file(json_data['b64'])


# POST URLS
@web.route('/get-posts', methods=['GET'])
def get_posts():
    return PostController().get_posts()


@web.route('/add-post', methods=['POST'])
def create_post():
    post = request.get_json()
    PostController().create_post(post)
    return jsonify({'response': 'Ok'})


@web.route('/update-post-position', methods=['POST'])
def update_post_position():
    data = request.get_json()
    return PostController().update_post_position(data)
