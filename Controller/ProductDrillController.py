from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Service.ProductDrillService import ProductDrillService
from ..Model.ProductDrillModel import ProductDrillModel
import json


productDrill = Blueprint('productDrill', __name__)
CORS(productDrill, resources={r"/*": {"origins": "*"}})


@productDrill.route('/get-products-drill', methods=['GET'])
def get_all():
    return ProductDrillService(ProductDrillModel).get_product()


@productDrill.route('/create-product-drill', methods=['POST'])
def create():
    ProductDrillService(ProductDrillModel).create_product(request.get_json())
    ProductDrillService(ProductDrillModel).update_position(json.loads(ProductDrillService(ProductDrillModel).get_all()))
    return jsonify({'response': 'Ok'})


@productDrill.route('/update-product-drill', methods=['POST'])
def update():
    ProductDrillService(ProductDrillModel).update_product(request.get_json())
    return jsonify({'response': 'Ok'})


@productDrill.route('/delete-product-drill', methods=['POST'])
def delete():
    ProductDrillService(ProductDrillModel).delete(request.get_json())
    ProductDrillService(ProductDrillModel).update_position(json.loads(ProductDrillService(ProductDrillModel).get_all()))
    return jsonify({'response': 'Ok'})


@productDrill.route('/update-product-drill-position', methods=['POST'])
def update_position():
    return ProductDrillService(ProductDrillModel).update_position(request.get_json())


@productDrill.route('/bulk-activate-products-drill', methods=['POST'])
def bulk_activate():
    ProductDrillService(ProductDrillModel).bulk_activate(request.get_json())
    return jsonify({'response': 'Ok'})


@productDrill.route('/bulk-deactivate-products-drill', methods=['POST'])
def bulk_deactivate():
    ProductDrillService(ProductDrillModel).bulk_deactivate(request.get_json())
    return jsonify({'response': 'Ok'})


@productDrill.route('/bulk-delete-products-drill', methods=['POST'])
def bulk_delete():
    ProductDrillService(ProductDrillModel).bulk_delete(request.get_json())
    ProductDrillService(ProductDrillModel).update_position(json.loads(ProductDrillService(ProductDrillModel).get_all()))
    return jsonify({'response': 'Ok'})
