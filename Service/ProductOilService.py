from ..Model.ProductOilModel import ProductOilModel
from ..Model.BrandModel import BrandModel
from ..Model.CategoryModel import CategoryModel
from ..Helper.JSONEncoder import JSONEncoder
from .Service import Service
from ..Config.database import db
from bson.json_util import dumps


class ProductOilService(Service):

    @staticmethod
    def get_product():
        result = list(ProductOilModel.objects.aggregate(*[
            {
                '$lookup': {
                    'from': 'brands',
                    'localField': 'brand_id',
                    'foreignField': '_id',
                    'as': 'brand'
                }
            },
            {
                '$lookup': {
                    'from': 'categories',
                    'localField': 'category_id',
                    'foreignField': '_id',
                    'as': 'category'
                }
            },
            {'$unwind': "$brand"},
            {'$unwind': "$category"},
            {
                '$addFields': {
                    'subcategory': {
                        '$reduce': {
                            'input': "$category.subCategories",
                            'initialValue': 'null',
                            'in': {
                                '$cond': [
                                    {'$eq': ["$$this.sub_id", "$subCategory_id"]},
                                    "$$this",
                                    "$$value"
                                ]
                            }
                        }
                    }
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
    def get_product_by_slug(data):
        return dumps(db().products_oil.find({'slug': data['slug']}))

    @staticmethod
    def create_product(product) -> ProductOilModel:
        default_subcategory = {'sub_id': {'$oid': '5f097afbe6978021fd00fdef'}}
        p = ProductOilModel()
        p.brand_id = BrandModel(id=product['brand']['_id']['$oid'])
        p.category_id = CategoryModel(id=product['category']['_id']['$oid'])
        p.subCategory_id = product \
            .get('subcategory', default_subcategory) \
            .get('sub_id', default_subcategory['sub_id']) \
            .get('$oid', default_subcategory['sub_id']['$oid'])
        p.position = 0
        p.active = product.get('active', 1)
        p.slug = product['slug']
        p.name = product['name']
        p.description = product['description']
        p.spec = product['spec']
        p.imgPath = product['imgPath']
        p.pdf1Path = product['pdf1Path']
        p.pdf2Path = product['pdf2Path']
        p.save()
        return p

    @staticmethod
    def update_product(product):
        ProductOilModel.objects(id=product['_id']['$oid']).update(**{
            "set__brand_id": BrandModel(id=product['brand']['_id']['$oid']),
            "set__category_id": CategoryModel(id=product['category']['_id']['$oid']),
            "set__subCategory_id": product['subcategory']['sub_id']['$oid'],
            "set__slug": product['slug'],
            "set__name": product['name'],
            "set__description": product['description'],
            "set__spec": product['spec'],
            "set__imgPath": product['imgPath'],
            "set__pdf1Path": product['pdf1Path'],
            "set__pdf2Path": product['pdf2Path'],
            "set__active": product.get('active', 1),
        })
