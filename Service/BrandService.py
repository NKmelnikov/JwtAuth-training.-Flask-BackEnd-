from flask import jsonify
from bson import json_util
from ..Model.BrandModel import BrandModel


class BrandService:

    @staticmethod
    def get_brands() -> BrandModel:
        return BrandModel.objects().order_by('position').to_json()

    @staticmethod
    def get_brands_sorted_by_date() -> BrandModel:
        return BrandModel.objects().order_by('-createdAt').to_json()

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
            "set__brandName": brand['brandTitle'],
            "set__brandImgPath": brand['brandImgPath'],
            "set__active": brand.get('active', 0),
        })

    @staticmethod
    def delete_brand(brand):
        BrandModel.objects(id=brand['_id']['$oid']).delete()

    @staticmethod
    def update_brand_position(data):
        for i, item in enumerate(data):
            BrandModel.objects(id=item['_id']['$oid']).update_one(set__position=i + 1)
        return BrandModel.objects().to_json()

    @staticmethod
    def bulk_activate_brands(data):
        for i, item in enumerate(data):
            BrandModel.objects(id=item['_id']['$oid']).update_one(set__active=1)

    @staticmethod
    def bulk_deactivate_brands(data):
        for i, item in enumerate(data):
            BrandModel.objects(id=item['_id']['$oid']).update_one(set__active=0)

    @staticmethod
    def bulk_delete_brands(data):
        for i, item in enumerate(data):
            BrandModel.objects(id=item['_id']['$oid']).delete()
