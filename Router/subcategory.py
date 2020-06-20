from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.CategoryController import CategoryController

subcategory = Blueprint('subcategory', __name__)
CORS(subcategory, resources={r"/*": {"origins": "*"}})


@subcategory.route('/create-subcategory', methods=['POST'])
def create_sub_category():
    CategoryController().create_sub_category(request.get_json())
    return jsonify({'response': 'Ok'})


@subcategory.route('/update-subcategory', methods=['POST'])
def update_sub_category():
    CategoryController().update_sub_category(request.get_json())
    return jsonify({'response': 'Ok'})


@subcategory.route('/delete-subcategory', methods=['POST'])
def delete_sub_category():
    CategoryController().delete_sub_category(request.get_json())
    return jsonify({'response': 'Ok'})


@subcategory.route('/update-subcategory-position', methods=['POST'])
def update_sub_category_position():
    return CategoryController().update_sub_category_position(request.get_json())


@subcategory.route('/bulk-activate-subcategories', methods=['POST'])
def bulk_activate_sub_categories():
    CategoryController().bulk_activate_sub_categories(request.get_json())
    return jsonify({'response': 'Ok'})


@subcategory.route('/bulk-deactivate-subcategories', methods=['POST'])
def bulk_deactivate_sub_categories():
    CategoryController().bulk_deactivate_sub_categories(request.get_json())
    return jsonify({'response': 'Ok'})


@subcategory.route('/bulk-delete-subcategories', methods=['POST'])
def bulk_delete_sub_categories():
    CategoryController().bulk_delete_sub_categories(request.get_json())
    return jsonify({'response': 'Ok'})
