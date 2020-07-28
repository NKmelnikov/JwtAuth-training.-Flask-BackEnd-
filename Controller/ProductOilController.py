from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Service.ProductOilService import ProductOilService
from ..Model.ProductOilModel import ProductOilModel
import json


productOil = Blueprint('productOil', __name__)
CORS(productOil, resources={r"/*": {"origins": "*"}})


@productOil.route('/get-products-oil', methods=['GET'])
def get_all():
    return ProductOilService(ProductOilModel).get_product()


@productOil.route('/get-product-oil-by-slug', methods=['POST'])
def get_product_by_slug():
    return ProductOilService(ProductOilModel).get_product_by_slug(request.get_json())


@productOil.route('/create-product-oil', methods=['POST'])
def create():
    ProductOilService(ProductOilModel).create_product(request.get_json())
    ProductOilService(ProductOilModel).update_position(json.loads(ProductOilService(ProductOilModel).get_all()))
    return jsonify({'response': 'Ok'})


@productOil.route('/update-product-oil', methods=['POST'])
def update():
    ProductOilService(ProductOilModel).update_product(request.get_json())
    return jsonify({'response': 'Ok'})


@productOil.route('/delete-product-oil', methods=['POST'])
def delete():
    ProductOilService(ProductOilModel).delete(request.get_json())
    ProductOilService(ProductOilModel).update_position(json.loads(ProductOilService(ProductOilModel).get_all()))
    return jsonify({'response': 'Ok'})


@productOil.route('/update-product-oil-position', methods=['POST'])
def update_position():
    return ProductOilService(ProductOilModel).update_position(request.get_json())


@productOil.route('/bulk-activate-products-oil', methods=['POST'])
def bulk_activate():
    ProductOilService(ProductOilModel).bulk_activate(request.get_json())
    return jsonify({'response': 'Ok'})


@productOil.route('/bulk-deactivate-products-oil', methods=['POST'])
def bulk_deactivate():
    ProductOilService(ProductOilModel).bulk_deactivate(request.get_json())
    return jsonify({'response': 'Ok'})


@productOil.route('/bulk-delete-products-oil', methods=['POST'])
def bulk_delete():
    ProductOilService(ProductOilModel).bulk_delete(request.get_json())
    ProductOilService(ProductOilModel).update_position(json.loads(ProductOilService(ProductOilModel).get_all()))
    return jsonify({'response': 'Ok'})
