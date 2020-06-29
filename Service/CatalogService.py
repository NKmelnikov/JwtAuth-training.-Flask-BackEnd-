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
    def create_catalog(_catalog) -> CatalogModel:
        catalog = CatalogModel()
        catalog.brand = BrandModel(id=_catalog['brand']['_id']['$oid'])
        catalog.position = 0
        catalog.active = _catalog.get('active', 0)
        catalog.catalogName = _catalog['catalogName']
        catalog.catalogPdfPath = _catalog['catalogPdfPath']
        catalog.save()
        return catalog

    @staticmethod
    def update_catalog(catalog):
        CatalogModel.objects(id=catalog['_id']['$oid']).update(**{
            "set__brand": BrandModel(id=catalog['brand']['_id']['$oid']),
            "set__catalogName": catalog['catalogName'],
            "set__catalogPdfPath": catalog['catalogPdfPath'],
            "set__active": catalog.get('active', 0),
        })

