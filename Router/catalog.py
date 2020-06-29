from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Service.CatalogService import CatalogService
from ..Model.CatalogModel import CatalogModel
import json

catalog = Blueprint('catalog', __name__)
CORS(catalog, resources={r"/*": {"origins": "*"}})


@catalog.route('/get-catalogs', methods=['GET'])
def get_all():
    return CatalogService(CatalogModel).get_catalogs()


@catalog.route('/create-catalog', methods=['POST'])
def create():
    CatalogService(CatalogModel).create_catalog(request.get_json())
    CatalogService(CatalogModel).update_position(json.loads(CatalogService(CatalogModel).get_all()))
    return jsonify({'response': 'Ok'})


@catalog.route('/update-catalog', methods=['POST'])
def update():
    CatalogService(CatalogModel).update_catalog(request.get_json())
    return jsonify({'response': 'Ok'})


@catalog.route('/delete-catalog', methods=['POST'])
def delete():
    CatalogService(CatalogModel).delete(request.get_json())
    CatalogService(CatalogModel).update_position(json.loads(CatalogService(CatalogModel).get_all()))
    return jsonify({'response': 'Ok'})


@catalog.route('/update-catalog-position', methods=['POST'])
def update_position():
    return CatalogService(CatalogModel).update_position(request.get_json())


@catalog.route('/bulk-activate-catalogs', methods=['POST'])
def bulk_activate():
    CatalogService(CatalogModel).bulk_activate(request.get_json())
    return jsonify({'response': 'Ok'})


@catalog.route('/bulk-deactivate-catalogs', methods=['POST'])
def bulk_deactivate():
    CatalogService(CatalogModel).bulk_deactivate(request.get_json())
    return jsonify({'response': 'Ok'})


@catalog.route('/bulk-delete-catalogs', methods=['POST'])
def bulk_delete():
    CatalogService(CatalogModel).bulk_delete(request.get_json())
    CatalogService(CatalogModel).update_position(json.loads(CatalogService(CatalogModel).get_all()))
    return jsonify({'response': 'Ok'})
