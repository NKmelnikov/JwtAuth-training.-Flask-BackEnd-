from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Service.BrandService import BrandService
from ..Model.BrandModel import BrandModel
import json

brand = Blueprint('brand', __name__)
CORS(brand, resources={r"/*": {"origins": "*"}})


@brand.route('/get-brands', methods=['GET'])
def get_all():
    return BrandService(BrandModel).get_all()


@brand.route('/create-brand', methods=['POST'])
def create_brand():
    BrandService(BrandModel).create_brand(request.get_json())
    BrandService(BrandModel).update_position(json.loads(BrandService(BrandModel).get_all()))
    return jsonify({'response': 'Ok'})


@brand.route('/update-brand', methods=['POST'])
def update_brand():
    BrandService(BrandModel).update_brand(request.get_json())
    return jsonify({'response': 'Ok'})


@brand.route('/delete-brand', methods=['POST'])
def delete():
    BrandService(BrandModel).delete(request.get_json())
    BrandService(BrandModel).update_position(json.loads(BrandService(BrandModel).get_all()))
    return jsonify({'response': 'Ok'})


@brand.route('/update-brand-position', methods=['POST'])
def update_position():
    return BrandService(BrandModel).update_position(request.get_json())


@brand.route('/bulk-activate-brands', methods=['POST'])
def bulk_activate():
    BrandService(BrandModel).bulk_activate(request.get_json())
    return jsonify({'response': 'Ok'})


@brand.route('/bulk-deactivate-brands', methods=['POST'])
def bulk_deactivate():
    BrandService(BrandModel).bulk_deactivate(request.get_json())
    return jsonify({'response': 'Ok'})


@brand.route('/bulk-delete-brands', methods=['POST'])
def bulk_delete():
    BrandService(BrandModel).bulk_delete(request.get_json())
    BrandService(BrandModel).update_position(json.loads(BrandService(BrandModel).get_all()))
    return jsonify({'response': 'Ok'})
