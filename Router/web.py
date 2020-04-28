from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from ..Controller.UserController import UserController
from ..Controller.PostController import PostController

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


# POST URLS
@web.route('/getPosts', methods=['GET'])
def get_posts():
    return PostController().get_posts()


@web.route('/addPost', methods=['POST'])
def create_post():
    json_data = request.get_json()
    post = {
        'position': json_data['position'],
        'active': json_data['active'],
        'postImgPath': json_data['postImgPath'],
        'postTitle': json_data['postTitle'],
        'postShortText': json_data['postShortText'],
        'postArticle': json_data['postArticle']
    }

    PostController().create_post(post)
    return jsonify({'response': 'Ok'})
