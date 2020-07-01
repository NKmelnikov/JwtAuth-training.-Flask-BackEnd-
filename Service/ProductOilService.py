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
                    'as': 'category '
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
        p = ProductOilModel()
        p.brand_id = BrandModel(id=product['brand_id']['$oid'])
        p.category_id = CategoryModel(id=product['category_id']['$oid'])
        p.subCategory_id = product['subCategory_id']['$oid']
        p.position = 0
        p.active = product.get('active', 0)
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
            "set__brand_id": BrandModel(id=product['brand_id']['$oid']),
            "set__category_id": CategoryModel(id=product['category_id']['$oid']),
            "set__subCategory_id": product['subCategory_id']['$oid'],
            "set__productName": product['productName'],
            "set__productDescription": product['productDescription'],
            "set__productSpec": product['productSpec'],
            "set__productImgPath": product['productImgPath'],
            "set__productPdf1Path": product['productPdf1Path'],
            "set__productPdf2Path": product['productPdf2Path'],
            "set__active": product.get('active', 0),
        })

