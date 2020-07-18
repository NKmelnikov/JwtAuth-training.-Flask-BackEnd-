from ..Model.ProductOilModel import ProductOilModel
from ..Model.BrandModel import BrandModel
from ..Model.CategoryModel import CategoryModel
from ..Helper.JSONEncoder import JSONEncoder
from .Service import Service


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
        p.productSlug = product['productSlug']
        p.productName = product['productName']
        p.productDescription = product['productDescription']
        p.productSpec = product['productSpec']
        p.productImgPath = product['productImgPath']
        p.productPdf1Path = product['productPdf1Path']
        p.productPdf2Path = product['productPdf2Path']
        p.save()
        return p

    @staticmethod
    def update_product(product):
        ProductOilModel.objects(id=product['_id']['$oid']).update(**{
            "set__brand_id": BrandModel(id=product['brand']['_id']['$oid']),
            "set__category_id": CategoryModel(id=product['category']['_id']['$oid']),
            "set__subCategory_id": product['subcategory']['sub_id']['$oid'],
            "set__productSlug": product['productSlug'],
            "set__productName": product['productName'],
            "set__productDescription": product['productDescription'],
            "set__productSpec": product['productSpec'],
            "set__productImgPath": product['productImgPath'],
            "set__productPdf1Path": product['productPdf1Path'],
            "set__productPdf2Path": product['productPdf2Path'],
            "set__active": product.get('active', 1),
        })
