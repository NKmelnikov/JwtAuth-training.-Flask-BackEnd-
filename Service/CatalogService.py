from ..Model.CatalogModel import CatalogModel
from ..Model.BrandModel import BrandModel
from ..Helper.JSONEncoder import JSONEncoder
from .Service import Service


class CatalogService(Service):

    @staticmethod
    def get_catalogs():
        result = list(CatalogModel.objects.aggregate(*[
            {
                '$lookup': {
                    'from': 'brands',
                    'localField': 'brand',
                    'foreignField': '_id',
                    'as': 'brands'
                }
            },
            {
                '$sort': {
                    'position': 1
                }
            }
        ]))

        return JSONEncoder().encode(result)

    @staticmethod
    def create_catalog(catalog) -> CatalogModel:
        c = CatalogModel()
        c.brand = BrandModel(id=catalog['brand']['_id']['$oid'])
        c.position = 0
        c.active = catalog.get('active', 0)
        c.catalogName = catalog['catalogName']
        c.catalogPdfPath = catalog['catalogPdfPath']
        c.save()
        return c

    @staticmethod
    def update_catalog(catalog):
        CatalogModel.objects(id=catalog['_id']['$oid']).update(**{
            "set__brand": BrandModel(id=catalog['brand']['_id']['$oid']),
            "set__catalogName": catalog['catalogName'],
            "set__catalogPdfPath": catalog['catalogPdfPath'],
            "set__active": catalog.get('active', 0),
        })

