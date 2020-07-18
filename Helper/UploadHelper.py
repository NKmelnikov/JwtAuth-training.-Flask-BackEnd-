import base64
import os
from io import BytesIO
from PIL import Image
from flask import send_from_directory
from flask_ckeditor import *


class UploadHelper:

    @staticmethod
    def upload_pdf(file):
        path = f"{current_app.config['UPLOAD_PATH']}pdf/{file.filename}"
        path = UploadHelper.unique_filename(path)
        file.save(path)
        # TODO deal with static methods
        return jsonify({'path': path, 'name': file.filename})

    @staticmethod
    def upload_img_from_b64(data):
        b64_string = data['b64']
        name = data['name']
        starter = b64_string.find(',')
        image_data = b64_string[starter + 1:]
        image_data = bytes(image_data, encoding="ascii")
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        path = f"{current_app.config['UPLOAD_PATH']}img/{name}"
        path = UploadHelper.unique_filename(path)
        im.save(path)
        return jsonify({'path': path})

    # TODO detecting extension

    @staticmethod
    def ck_upload(_request):
        f = _request.files.get('upload')
        extension = f.filename.split('.')[1].lower()
        name = f.filename.split('.')[0].lower()
        if extension not in ['jpg', 'gif', 'png', 'jpeg']:
            return jsonify({'response': 'invalid extension'})
        f.filename = f"{name}.{extension}"

        path = f"{current_app.config['UPLOAD_PATH']}img/{f.filename}"
        path = UploadHelper.unique_filename(path)
        f.save(path)

        url = url_for('helper.uploaded_images', filename=f.filename)
        return upload_success(url=f"{current_app.config['SERVER_URL']}{url}")

    @staticmethod
    def uploaded_images(filename):
        path = f"{current_app.config['UPLOAD_PATH']}img/"
        return send_from_directory(path, filename)

    @staticmethod
    def uploaded_pdfs(filename):
        path = f"{current_app.config['UPLOAD_PATH']}pdf/"
        return send_from_directory(path, filename)

    @staticmethod
    def get_files_in_folder(req):
        path = f"{os.getcwd()}/files/{req['folder_name']}"
        list_of_files = []

        for filename in os.listdir(path):
            list_of_files.append(filename)

        return jsonify({'list_of_files': list_of_files})

    @staticmethod
    def unique_filename(path):
        filename, extension = os.path.splitext(path)
        counter = 1

        while os.path.exists(path):
            path = filename + " (" + str(counter) + ")" + extension
            counter += 1

        return path
