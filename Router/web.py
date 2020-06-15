from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.UserController import UserController
from ..Helper.UploadHelper import UploadHelper

web = Blueprint('web', __name__)
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
