from ..Service.BrandService import BrandService
import json


class BrandController:

    @staticmethod
    def get_brands():
        return BrandService().get_brands()

    @staticmethod
    def create_brand(brand):
        BrandService().create_brand(brand)
        BrandService().update_brand_position(json.loads(BrandService().get_brands_sorted_by_date()))

    @staticmethod
    def update_brand(brand):
        BrandService().update_brand(brand)

    @staticmethod
    def delete_brand(brand):
        BrandService().delete_brand(brand)

    @staticmethod
    def update_brand_position(data):
        return BrandService().update_brand_position(data)

    @staticmethod
    def bulk_activate_brands(data):
        BrandService().bulk_activate_brands(data)
        BrandService().update_brand_position(json.loads(BrandService().get_brands()))

    @staticmethod
    def bulk_deactivate_brands(data):
        BrandService().bulk_deactivate_brands(data)
        BrandService().update_brand_position(json.loads(BrandService().get_brands()))

    @staticmethod
    def bulk_delete_brands(data):
        BrandService().bulk_delete_brands(data)
        BrandService().update_brand_position(json.loads(BrandService().get_brands()))
