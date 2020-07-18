from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Service.UserService import UserService
from ..Helper.UploadHelper import UploadHelper

helper = Blueprint('helper', __name__)
CORS(helper, resources={r"/*": {"origins": "*"}})


@helper.route('/')
def welcome():
    return jsonify({'response': 'welcome to server'})


@helper.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    UserService().create_account(email, password)
    return jsonify({'response': 'Ok'})


@helper.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    return UserService().create_auth_token(email, password)


@helper.route('/ck-upload', methods=['POST'])
def ck_upload():
    return UploadHelper().ck_upload(request)


@helper.route('/files/img/<filename>')
def uploaded_images(filename):
    return UploadHelper().uploaded_images(filename)


@helper.route('/files/pdf/<filename>')
def uploaded_pdfs(filename):
    return UploadHelper().uploaded_pdfs(filename)


@helper.route('/upload-img-from-b64', methods=['POST'])
def upload_img_from_b64():
    return UploadHelper().upload_img_from_b64(request.get_json())


@helper.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    return UploadHelper().upload_pdf(request.files['pdf_file'])


@helper.route('/get-files-in-folder', methods=['POST'])
def get_files_in_folder():
    return UploadHelper().get_files_in_folder(request.get_json())
