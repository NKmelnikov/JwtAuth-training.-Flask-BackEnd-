from flask import Blueprint, request, jsonify
from flask_cors import CORS

product = Blueprint('product', __name__)
CORS(product, resources={r"/*": {"origins": "*"}})


@product.route('/test')
def welcome():
    return jsonify({'response': 'welcome to test11'})
