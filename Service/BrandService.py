from ..Model.BrandModel import BrandModel
from .Service import Service


class BrandService(Service):

    @staticmethod
    def create_brand(_brand) -> BrandModel:
        brand = BrandModel()
        brand.position = 0
        brand.active = _brand.get('active', 0)
        brand.brandName = _brand['brandName']
        brand.brandImgPath = _brand['brandImgPath']
        brand.save()
        return brand

    @staticmethod
    def update_brand(brand):
        BrandModel.objects(id=brand['_id']['$oid']).update(**{
            "set__brandName": brand['brandName'],
            "set__brandImgPath": brand['brandImgPath'],
            "set__active": brand.get('active', 0),
        })
