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


@web.route('/ck-upload', methods=['POST'])
def ck_upload():
    return UploadHelper().ck_upload(request)


@web.route('/files/<filename>')
def uploaded_files(filename):
    return UploadHelper().uploaded_files(filename)


@web.route('/upload-file', methods=['POST'])
def upload_file():
    json_data = request.get_json()
    return UploadHelper().upload_file(json_data)


# POST URLS
@web.route('/get-posts', methods=['GET'])
def get_posts():
    return PostController().get_posts()


@web.route('/create-post', methods=['POST'])
def create_post():
    PostController().create_post(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/update-post', methods=['POST'])
def update_post():
    PostController().update_post(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/delete-post', methods=['POST'])
def delete_post():
    PostController().delete_post(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/update-post-position', methods=['POST'])
def update_post_position():
    data = request.get_json()
    return PostController().update_post_position(data)


@web.route('/bulk-activate', methods=['POST'])
def bulk_activate():
    PostController().bulk_activate(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/bulk-deactivate', methods=['POST'])
def bulk_deactivate():
    PostController().bulk_deactivate(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/bulk-delete', methods=['POST'])
def bulk_delete():
    PostController().bulk_delete(request.get_json())
    return jsonify({'response': 'Ok'})
