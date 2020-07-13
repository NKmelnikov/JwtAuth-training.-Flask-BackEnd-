from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Service.CategoryService import CategoryService
from ..Model.CategoryModel import CategoryModel
import json

category = Blueprint('category', __name__)
CORS(category, resources={r"/*": {"origins": "*"}})


@category.route('/get-categories', methods=['GET'])
def get_categories():
    return CategoryService(CategoryModel).get_all()


@category.route('/get-category-by-id', methods=['POST'])
def get_category_by_id():
    return CategoryService(CategoryModel).get_category_by_id(request.get_json(), 'position', 1)


@category.route('/create-category', methods=['POST'])
def create_category():
    CategoryService(CategoryModel).create_category(request.get_json())
    CategoryService(CategoryModel).update_position(json.loads(CategoryService(CategoryModel).get_all()))

    return jsonify({'response': 'Ok'})


@category.route('/update-category', methods=['POST'])
def update_category():
    CategoryService(CategoryModel).update_category(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/delete-category', methods=['POST'])
def delete_category():
    CategoryService(CategoryModel).delete(request.get_json())
    CategoryService(CategoryModel).update_position(json.loads(CategoryService(CategoryModel).get_all()))

    return jsonify({'response': 'Ok'})


@category.route('/update-category-position', methods=['POST'])
def update_category_position():
    return CategoryService(CategoryModel).update_position(request.get_json())


@category.route('/bulk-activate-categories', methods=['POST'])
def bulk_activate_categories():
    CategoryService(CategoryModel).bulk_activate(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/bulk-deactivate-categories', methods=['POST'])
def bulk_deactivate_categories():
    CategoryService(CategoryModel).bulk_deactivate(request.get_json())
    return jsonify({'response': 'Ok'})


@category.route('/bulk-delete-categories', methods=['POST'])
def bulk_delete_categories():
    CategoryService(CategoryModel).bulk_delete(request.get_json())
    CategoryService(CategoryModel).update_position(json.loads(CategoryService(CategoryModel).get_all()))

    return jsonify({'response': 'Ok'})
