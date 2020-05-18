from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.UserController import UserController
from ..Controller.PostController import PostController
from ..Controller.BrandController import BrandController
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


# POST URLS======================================
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


@web.route('/bulk-activate-posts', methods=['POST'])
def bulk_activate_posts():
    PostController().bulk_activate_posts(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/bulk-deactivate-posts', methods=['POST'])
def bulk_deactivate_posts():
    PostController().bulk_deactivate_posts(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/bulk-delete-posts', methods=['POST'])
def bulk_delete_posts():
    PostController().bulk_delete_posts(request.get_json())
    return jsonify({'response': 'Ok'})


# BRAND URLS======================================
@web.route('/get-brands', methods=['GET'])
def get_brands():
    return BrandController().get_brands()


@web.route('/create-brand', methods=['POST'])
def create_brand():
    BrandController().create_brand(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/update-brand', methods=['POST'])
def update_brand():
    BrandController().update_brand(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/delete-brand', methods=['POST'])
def delete_brand():
    BrandController().delete_brand(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/update-brand-position', methods=['POST'])
def update_brand_position():
    data = request.get_json()
    return BrandController().update_brand_position(data)


@web.route('/bulk-activate-brands', methods=['POST'])
def bulk_activate_brands():
    BrandController().bulk_activate_brands(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/bulk-deactivate-brands', methods=['POST'])
def bulk_deactivate_brands():
    BrandController().bulk_deactivate_brands(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/bulk-delete-brands', methods=['POST'])
def bulk_delete_brands():
    BrandController().bulk_delete_brands(request.get_json())
    return jsonify({'response': 'Ok'})
