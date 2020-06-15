from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.CategoryController import CategoryController

category_oil = Blueprint('category_oil', __name__)
CORS(category_oil, resources={r"/*": {"origins": "*"}})


@category_oil.route('/get-categories-oil', methods=['GET'])
def get_categories_oil():
    return CategoryController().get_categories_oil()


@category_oil.route('/create-category-oil', methods=['POST'])
def create_category_oil():
    CategoryController().create_category_oil(request.get_json())
    return jsonify({'response': 'Ok'})


@category_oil.route('/create-sub-category-oil', methods=['POST'])
def create_sub_category_oil():
    CategoryController().create_sub_category_oil(request.get_json())
    return jsonify({'response': 'Ok'})


@category_oil.route('/update-category-oil', methods=['POST'])
def update_category_oil():
    CategoryController().update_category_oil(request.get_json())
    return jsonify({'response': 'Ok'})


@category_oil.route('/delete-category-oil', methods=['POST'])
def delete_category_oil():
    CategoryController().delete_category_oil(request.get_json())
    return jsonify({'response': 'Ok'})


@category_oil.route('/update-category-position-oil', methods=['POST'])
def update_category_position_oil():
    return CategoryController().update_category_position_oil(request.get_json())


@category_oil.route('/bulk-activate-categories-oil', methods=['POST'])
def bulk_activate_categories_oil():
    CategoryController().bulk_activate_categories_oil(request.get_json())
    return jsonify({'response': 'Ok'})


@category_oil.route('/bulk-deactivate-categories-oil', methods=['POST'])
def bulk_deactivate_categories_oil():
    CategoryController().bulk_deactivate_categories_oil(request.get_json())
    return jsonify({'response': 'Ok'})


@category_oil.route('/bulk-delete-categories-oil', methods=['POST'])
def bulk_delete_categories_oil():
    CategoryController().bulk_delete_categories_oil(request.get_json())
    return jsonify({'response': 'Ok'})
