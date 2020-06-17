from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.CategoryController import CategoryController

category = Blueprint('category', __name__)
CORS(category, resources={r"/*": {"origins": "*"}})


@category.route('/get-categories', methods=['GET'])
def get_categories():
    return CategoryController().get_categories()


@category.route('/get-categories-by-id', methods=['POST'])
def get_category_by_id():
    return CategoryController().get_category_by_id(request.get_json())


@category.route('/create-category', methods=['POST'])
def create_category():
    CategoryController().create_category(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/create-sub-category', methods=['POST'])
def create_sub_category():
    CategoryController().create_sub_category(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/update-category', methods=['POST'])
def update_category():
    CategoryController().update_category(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/update-sub-category', methods=['POST'])
def update_sub_category():
    CategoryController().update_sub_category(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/delete-category', methods=['POST'])
def delete_category():
    CategoryController().delete_category(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/delete-sub-category', methods=['POST'])
def delete_sub_category():
    CategoryController().delete_sub_category(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/update-category-position', methods=['POST'])
def update_category_position():
    return CategoryController().update_category_position(request.get_json())


@category.route('/bulk-activate-categories', methods=['POST'])
def bulk_activate_categories():
    CategoryController().bulk_activate_categories(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/bulk-deactivate-categories', methods=['POST'])
def bulk_deactivate_categories():
    CategoryController().bulk_deactivate_categories(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/bulk-delete-categories', methods=['POST'])
def bulk_delete_categories():
    CategoryController().bulk_delete_categories(request.get_json())
    return jsonify({'response': 'Ok'})
