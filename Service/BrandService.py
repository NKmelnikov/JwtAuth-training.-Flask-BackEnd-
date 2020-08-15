from ..Model.BrandModel import BrandModel
from .Service import Service
from ..Config.database import db
from bson.json_util import dumps


class BrandService(Service):

    @staticmethod
    def get_brand_by_slug(brand):
        request = list(db().brands.aggregate([
            {
                '$lookup': {
                    'from': 'catalogs',
                    'localField': '_id',
                    'foreignField': 'brand',
                    'as': 'catalogs'
                }
            },
            {
                '$sort': {
                    'position': 1
                }
            },
            {
                '$match': {
                    'slug': brand['brand']
                }
            }
        ]))

        return dumps(request[0]) or []

    @staticmethod
    def create_brand(brand) -> BrandModel:
        b = BrandModel()
        b.position = 0
        b.active = brand.get('active', 1)
        b.name = brand['name']
        b.slug = brand['slug']
        b.description = brand['description']
        b.imgPath = brand['imgPath']
        b.save()
        return b

    @staticmethod
    def update_brand(brand):
        BrandModel.objects(id=brand['_id']['$oid']).update(**{
            "set__slug": brand['slug'],
            "set__name": brand['name'],
            "description": brand['description'],
            "set__imgPath": brand['imgPath'],
            "set__active": brand.get('active', 0),
        })
