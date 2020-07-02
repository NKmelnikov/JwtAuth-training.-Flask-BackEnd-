from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Service.CategoryService import CategoryService
from ..Model.CategoryModel import CategoryModel
import json

subcategory = Blueprint('subcategory', __name__)
CORS(subcategory, resources={r"/*": {"origins": "*"}})


@subcategory.route('/create-subcategory', methods=['POST'])
def create_sub_category():
    category_id = {'id': request.get_json()['id']}
    CategoryService(CategoryModel).create_sub_category(request.get_json())
    category = json.loads(CategoryService(CategoryModel).get_category_by_id(category_id, 'position', 1))
    category['subCategories'].append(category_id['id'])
    CategoryService(CategoryModel).update_sub_category_position(category['subCategories'])
    return jsonify({'response': 'Ok'})


@subcategory.route('/update-subcategory', methods=['POST'])
def update_sub_category():
    CategoryService(CategoryModel).update_sub_category(request.get_json())
    return jsonify({'response': 'Ok'})


@subcategory.route('/delete-subcategory', methods=['POST'])
def delete_sub_category():
    category_id = {'id': request.get_json()['id']}
    CategoryService(CategoryModel).delete_sub_category(request.get_json())
    category = json.loads(CategoryService(CategoryModel).get_category_by_id(category_id, 'position', 1))
    category['subCategories'].append(category_id['id'])
    CategoryService(CategoryModel).update_sub_category_position(category['subCategories'])
    return jsonify({'response': 'Ok'})


@subcategory.route('/update-subcategory-position', methods=['POST'])
def update_sub_category_position():
    return CategoryService(CategoryModel).update_sub_category_position(request.get_json())


@subcategory.route('/bulk-activate-subcategories', methods=['POST'])
def bulk_activate_sub_categories():
    CategoryService(CategoryModel).bulk_activate_sub_categories(request.get_json())
    return jsonify({'response': 'Ok'})


@subcategory.route('/bulk-deactivate-subcategories', methods=['POST'])
def bulk_deactivate_sub_categories():
    CategoryService(CategoryModel).bulk_deactivate_sub_categories(request.get_json())
    return jsonify({'response': 'Ok'})


@subcategory.route('/bulk-delete-subcategories', methods=['POST'])
def bulk_delete_sub_categories():
    category_id = {'id': request.get_json()[-1]}
    CategoryService(CategoryModel).bulk_delete_sub_categories(request.get_json())
    category = json.loads(CategoryService(CategoryModel).get_category_by_id(category_id, 'position', 1))
    category['subCategories'].append(category_id['id'])
    CategoryService(CategoryModel).update_sub_category_position(category['subCategories'])
    return jsonify({'response': 'Ok'})
