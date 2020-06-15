from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.CatalogController import CatalogController

catalog = Blueprint('catalog', __name__)
CORS(catalog, resources={r"/*": {"origins": "*"}})


@catalog.route('/get-catalogs', methods=['GET'])
def get_catalogs():
    return CatalogController().get_catalogs()


@catalog.route('/create-catalog', methods=['POST'])
def create_catalog():
    CatalogController().create_catalog(request.get_json())
    return jsonify({'response': 'Ok'})


@catalog.route('/update-catalog', methods=['POST'])
def update_catalog():
    CatalogController().update_catalog(request.get_json())
    return jsonify({'response': 'Ok'})


@catalog.route('/delete-catalog', methods=['POST'])
def delete_catalog():
    CatalogController().delete_catalog(request.get_json())
    return jsonify({'response': 'Ok'})


@catalog.route('/update-catalog-position', methods=['POST'])
def update_catalog_position():
    return CatalogController().update_catalog_position(request.get_json())


@catalog.route('/bulk-activate-catalogs', methods=['POST'])
def bulk_activate_catalogs():
    CatalogController().bulk_activate_catalogs(request.get_json())
    return jsonify({'response': 'Ok'})


@catalog.route('/bulk-deactivate-catalogs', methods=['POST'])
def bulk_deactivate_catalogs():
    CatalogController().bulk_deactivate_catalogs(request.get_json())
    return jsonify({'response': 'Ok'})


@catalog.route('/bulk-delete-catalogs', methods=['POST'])
def bulk_delete_catalogs():
    CatalogController().bulk_delete_catalogs(request.get_json())
    return jsonify({'response': 'Ok'})
