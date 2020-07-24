from ..Model.ProductDrillModel import ProductDrillModel
from ..Model.BrandModel import BrandModel
from ..Model.CategoryModel import CategoryModel
from ..Helper.JSONEncoder import JSONEncoder
from .Service import Service


class ProductDrillService(Service):

    @staticmethod
    def get_product():
        result = list(ProductDrillModel.objects.aggregate(*[
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
    def create_product(product) -> ProductDrillModel:
        default_subcategory = {'sub_id': {'$oid': '5f097afbe6978021fd00fdef'}}
        p = ProductDrillModel()
        p.brand_id = BrandModel(id=product['brand']['_id']['$oid'])
        p.category_id = CategoryModel(id=product['category']['_id']['$oid'])
        p.subCategory_id = product\
            .get('subcategory', default_subcategory)\
            .get('sub_id', default_subcategory['sub_id'])\
            .get('$oid', default_subcategory['sub_id']['$oid'])
        p.position = 0
        p.active = product.get('active', 1)
        p.slug = product['slug']
        p.name = product['name']
        p.description = product['description']
        p.pdfPath = product['pdfPath']
        p.save()
        return p

    @staticmethod
    def update_product(product):
        ProductDrillModel.objects(id=product['_id']['$oid']).update(**{
            "set__brand_id": BrandModel(id=product['brand']['_id']['$oid']),
            "set__category_id": CategoryModel(id=product['category']['_id']['$oid']),
            "set__subCategory_id": product['subcategory']['sub_id']['$oid'],
            "set__slug": product['slug'],
            "set__name": product['name'],
            "set__description": product['description'],
            "set__pdfPath": product['pdfPath'],
            "set__active": product.get('active', 1),
        })
