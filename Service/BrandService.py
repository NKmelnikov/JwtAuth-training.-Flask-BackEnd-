from ..Model.BrandModel import BrandModel
from .Service import Service


class BrandService(Service):

    @staticmethod
    def create_brand(brand) -> BrandModel:
        b = BrandModel()
        b.position = 0
        b.active = brand.get('active', 1)
        b.name = brand['name']
        b.imgPath = brand['imgPath']
        b.save()
        return b

    @staticmethod
    def update_brand(brand):
        BrandModel.objects(id=brand['_id']['$oid']).update(**{
            "set__name": brand['name'],
            "set__imgPath": brand['imgPath'],
            "set__active": brand.get('active', 0),
        })
