from ..Model.BrandModel import BrandModel
from .Service import Service


class BrandService(Service):

    @staticmethod
    def create_brand(brand) -> BrandModel:
        b = BrandModel()
        b.position = 0
        b.active = brand.get('active', 1)
        b.brandName = brand['brandName']
        b.brandImgPath = brand['brandImgPath']
        b.save()
        return b

    @staticmethod
    def update_brand(brand):
        BrandModel.objects(id=brand['_id']['$oid']).update(**{
            "set__brandName": brand['brandName'],
            "set__brandImgPath": brand['brandImgPath'],
            "set__active": brand.get('active', 0),
        })
