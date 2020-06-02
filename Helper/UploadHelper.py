import base64
import os
from io import BytesIO
from PIL import Image
from flask import jsonify, send_from_directory
import calendar
import time
from flask import current_app
from flask_ckeditor import *


class UploadHelper:

    @staticmethod
    def upload_pdf(file):
        ts = calendar.timegm(time.gmtime())
        name = f"{ts}__{file.filename}"
        path = f"{current_app.config['UPLOAD_PATH']}/pdf/{name}"
        file.save(path)
        return jsonify({'path': path, 'name': file.filename})

    @staticmethod
    def upload_img_from_b64(data):
        ts = calendar.timegm(time.gmtime())
        b64_string = data['b64']
        name = f"{ts}__{data['name']}"
        starter = b64_string.find(',')
        image_data = b64_string[starter + 1:]
        image_data = bytes(image_data, encoding="ascii")
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        path = os.path.join(current_app.config['UPLOAD_PATH'], name)
        im.save(path)
        return jsonify({'path': path})

    # TODO detecting extension

    @staticmethod
    def ck_upload(request):
        ts = calendar.timegm(time.gmtime())
        f = request.files.get('upload')
        extension = f.filename.split('.')[1].lower()
        name = f.filename.split('.')[0].lower()
        if extension not in ['jpg', 'gif', 'png', 'jpeg']:
            return jsonify({'response': 'invalid extension'})
        f.filename = f"{ts}.{name}.{extension}"
        f.save(os.path.join(current_app.config['UPLOAD_PATH'], f.filename))
        url = url_for('app.uploaded_files', filename=f.filename)
        return upload_success(url=f"{current_app.config['SERVER_URL']}{url}")

    @staticmethod
    def uploaded_files(filename):
        path = current_app.config['UPLOAD_PATH']
        return send_from_directory(path, filename)
