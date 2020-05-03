import base64
from io import BytesIO
from PIL import Image
from flask import jsonify


class UploadHelper:

    @staticmethod
    def upload_file(b64_string):
        starter = b64_string.find(',')
        image_data = b64_string[starter + 1:]
        image_data = bytes(image_data, encoding="ascii")
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        im.save('image.jpg')
        return jsonify({'response': 'Ok'})

# TODO detecting extension
