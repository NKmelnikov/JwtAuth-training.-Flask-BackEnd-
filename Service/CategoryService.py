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
            {"_id": ObjectId("5ee787d532e45322e2de9e5d")},
            {'$push': {
                'subCategories': {
                    "_id": ObjectId(),
                    "createdAt": datetime.datetime.now(),
                    'position': sub.get('position', 1),
                    'active': sub.get('active', 0),
                    'subCategoryName': sub['subCategoryName'],
                    'subCategoryDescription': sub['subCategoryDescription']

                }
            }}
        )
