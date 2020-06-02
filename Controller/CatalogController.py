from ..Service.CatalogService import CatalogService
import json


class CatalogController:

    @staticmethod
    def get_catalogs():
        return CatalogService().get_catalogs()

    @staticmethod
    def create_catalog(catalog):
        CatalogService().create_catalog(catalog)
        CatalogService().update_catalog_position(json.loads(CatalogService().get_catalogs_sorted_by_date()))

    @staticmethod
    def update_catalog(catalog):
        CatalogService().update_catalog(catalog)

    @staticmethod
    def delete_catalog(catalog):
        CatalogService().delete_catalog(catalog)

    @staticmethod
    def update_catalog_position(data):
        return CatalogService().update_catalog_position(data)

    @staticmethod
    def bulk_activate_catalogs(data):
        CatalogService().bulk_activate_catalogs(data)
        CatalogService().update_catalog_position(json.loads(CatalogService().get_catalogs()))

    @staticmethod
    def bulk_deactivate_catalogs(data):
        CatalogService().bulk_deactivate_catalogs(data)
        CatalogService().update_catalog_position(json.loads(CatalogService().get_catalogs()))

    @staticmethod
    def bulk_delete_catalogs(data):
        CatalogService().bulk_delete_catalogs(data)
        CatalogService().update_catalog_position(json.loads(CatalogService().get_catalogs()))
