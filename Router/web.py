from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.UserController import UserController
from ..Controller.PostController import PostController
from ..Controller.BrandController import BrandController
from ..Controller.CatalogController import CatalogController
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


@web.route('/files/pdf/<filename>')
def uploaded_pdfs(filename):
    return UploadHelper().uploaded_pdfs(filename)


@web.route('/upload-img-from-b64', methods=['POST'])
def upload_img_from_b64():
    return UploadHelper().upload_img_from_b64(request.get_json())


@web.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    return UploadHelper().upload_pdf(request.files['pdf_file'])


# ======================================POST URLS======================================

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
    return PostController().update_post_position(request.get_json())


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


# ======================================BRAND URLS======================================

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
    return BrandController().update_brand_position(request.get_json())


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


# ======================================CATALOGS URLS======================================

@web.route('/get-catalogs', methods=['GET'])
def get_catalogs():
    return CatalogController().get_catalogs()


@web.route('/create-catalog', methods=['POST'])
def create_catalog():
    CatalogController().create_catalog(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/update-catalog', methods=['POST'])
def update_catalog():
    CatalogController().update_catalog(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/delete-catalog', methods=['POST'])
def delete_catalog():
    CatalogController().delete_catalog(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/update-catalog-position', methods=['POST'])
def update_catalog_position():
    return CatalogController().update_catalog_position(request.get_json())


@web.route('/bulk-activate-catalogs', methods=['POST'])
def bulk_activate_catalogs():
    CatalogController().bulk_activate_catalogs(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/bulk-deactivate-catalogs', methods=['POST'])
def bulk_deactivate_catalogs():
    CatalogController().bulk_deactivate_catalogs(request.get_json())
    return jsonify({'response': 'Ok'})


@web.route('/bulk-delete-catalogs', methods=['POST'])
def bulk_delete_catalogs():
    CatalogController().bulk_delete_catalogs(request.get_json())
    return jsonify({'response': 'Ok'})
