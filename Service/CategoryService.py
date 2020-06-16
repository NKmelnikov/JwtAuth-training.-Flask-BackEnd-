import json
from flask import jsonify
import datetime
from bson import json_util, ObjectId
from ..Model.CategoryOilModel import CategoryOilModel
from ..Model.SubCategoryOilModel import SubCategoryOilModel
from ..Helper.JSONEncoder import JSONEncoder
from ..Config.database import db


class CategoryService:

    @staticmethod
    def get_categories_oil():
        return CategoryOilModel.objects().order_by('position').to_json()

    @staticmethod
    def get_catalogs_sorted_by_date() -> CategoryOilModel:
        return CategoryOilModel.objects().order_by('-createdAt').to_json()

    @staticmethod
    def create_category_oil(category) -> CategoryOilModel:
        c = CategoryOilModel()
        c.position = 0
        c.active = category.get('active', 0)
        c.categoryName = category['categoryName']
        c.categoryDescription = category['categoryDescription']
        c.s = SubCategoryOilModel()
        c.save()
        return c

    @staticmethod
    def create_sub_category_oil(sub):
        db().categories_oil.update(
            {"_id": ObjectId(sub['_id'])},
            {'$push': {
                'subCategories': {
                    "sub_id": ObjectId(),
                    "createdAt": datetime.datetime.now(),
                    'position': sub.get('position', 1),
                    'active': sub.get('active', 0),
                    'subCategoryName': sub['subCategoryName'],
                    'subCategoryDescription': sub['subCategoryDescription']

                }
            }}
        )

    @staticmethod
    def update_category_oil(category):
        CategoryOilModel.objects(id=category['_id']['$oid']).update(**{
            "set__categoryName": category['categoryName'],
            "set__categoryDescription": category['categoryDescription'],
            "set__active": category.get('active', 0),
        })

    @staticmethod
    def update_sub_category_oil(sub):
        CategoryOilModel.objects(id=sub['_id']['$oid'], subCategories__sub_id=sub['sub_id']['$oid']).update(**{
            "set__subCategories__S__subCategoryName": sub['subCategoryName'],
            "set__subCategories__S__subCategoryDescription": sub['subCategoryDescription'],
            "set__subCategories__S__active": sub.get('active', 0),
        })

    @staticmethod
    def delete_category(catalog):
        CategoryOilModel.objects(id=catalog['_id']['$oid']).delete()

    @staticmethod
    def delete_sub_category(catalog):
        CategoryOilModel.objects(id=catalog['_id']['$oid']).delete()
