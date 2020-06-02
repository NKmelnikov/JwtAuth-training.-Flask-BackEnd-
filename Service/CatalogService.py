from flask import jsonify
from bson import json_util
from ..Model.CatalogModel import CatalogModel


class CatalogService:

    @staticmethod
    def get_catalogs() -> CatalogModel:
        return CatalogModel.objects().order_by('position').to_json()

    @staticmethod
    def get_catalogs_sorted_by_date() -> CatalogModel:
        return CatalogModel.objects().order_by('-createdAt').to_json()

    @staticmethod
    def create_catalog(_catalog) -> CatalogModel:
        catalog = CatalogModel()
        catalog.position = 0
        catalog.active = _catalog.get('active', 0)
        catalog.brandId = _catalog['brandId']
        catalog.catalogName = _catalog['catalogName']
        catalog.catalogPdfPath = _catalog['catalogPdfPath']
        catalog.save()
        return catalog

    @staticmethod
    def update_catalog(catalog):
        CatalogModel.objects(id=catalog['_id']['$oid']).update(**{
            "set__brandId": catalog['brandId'],
            "set__catalogName": catalog['catalogName'],
            "set__catalogPdfPath": catalog['catalogPdfPath'],
            "set__active": catalog.get('active', 0),
        })

    @staticmethod
    def delete_catalog(catalog):
        CatalogModel.objects(id=catalog['_id']['$oid']).delete()

    @staticmethod
    def update_catalog_position(data):
        for i, item in enumerate(data):
            CatalogModel.objects(id=item['_id']['$oid']).update_one(set__position=i + 1)
        return CatalogModel.objects().to_json()

    @staticmethod
    def bulk_activate_catalogs(data):
        for i, item in enumerate(data):
            CatalogModel.objects(id=item['_id']['$oid']).update_one(set__active=1)

    @staticmethod
    def bulk_deactivate_catalogs(data):
        for i, item in enumerate(data):
            CatalogModel.objects(id=item['_id']['$oid']).update_one(set__active=0)

    @staticmethod
    def bulk_delete_catalogs(data):
        for i, item in enumerate(data):
            CatalogModel.objects(id=item['_id']['$oid']).delete()
