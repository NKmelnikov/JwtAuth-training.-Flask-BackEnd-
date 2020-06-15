from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.BrandController import BrandController

brand = Blueprint('brand', __name__)
CORS(brand, resources={r"/*": {"origins": "*"}})


@brand.route('/get-brands', methods=['GET'])
def get_brands():
    return BrandController().get_brands()


@brand.route('/create-brand', methods=['POST'])
def create_brand():
    BrandController().create_brand(request.get_json())
    return jsonify({'response': 'Ok'})


@brand.route('/update-brand', methods=['POST'])
def update_brand():
    BrandController().update_brand(request.get_json())
    return jsonify({'response': 'Ok'})


@brand.route('/delete-brand', methods=['POST'])
def delete_brand():
    BrandController().delete_brand(request.get_json())
    return jsonify({'response': 'Ok'})


@brand.route('/update-brand-position', methods=['POST'])
def update_brand_position():
    return BrandController().update_brand_position(request.get_json())


@brand.route('/bulk-activate-brands', methods=['POST'])
def bulk_activate_brands():
    BrandController().bulk_activate_brands(request.get_json())
    return jsonify({'response': 'Ok'})


@brand.route('/bulk-deactivate-brands', methods=['POST'])
def bulk_deactivate_brands():
    BrandController().bulk_deactivate_brands(request.get_json())
    return jsonify({'response': 'Ok'})


@brand.route('/bulk-delete-brands', methods=['POST'])
def bulk_delete_brands():
    BrandController().bulk_delete_brands(request.get_json())
    return jsonify({'response': 'Ok'})
