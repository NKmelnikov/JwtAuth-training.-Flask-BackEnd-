import json
from flask import jsonify
import datetime
from bson import json_util, ObjectId
from ..Model.CategoryModel import CategoryModel
from ..Model.SubCategoryModel import SubCategoryModel
from ..Helper.JSONEncoder import JSONEncoder
from ..Config.database import db


class CategoryService:

    @staticmethod
    def get_categories():
        return CategoryModel.objects().order_by('position').to_json()

    @staticmethod
    def get_category_by_id(category_id):
        return CategoryModel.objects().get(id=category_id['id']).to_json()

    @staticmethod
    def get_categories_sorted_by_date() -> CategoryModel:
        return CategoryModel.objects().order_by('-createdAt').to_json()

    @staticmethod
    def create_category(category) -> CategoryModel:
        c = CategoryModel()
        c.position = 1
        c.active = category.get('active', 0)
        c.categoryType = category['categoryType']
        c.categoryName = category['categoryName']
        c.categoryDescription = category['categoryDescription']
        c.s = SubCategoryModel()
        c.save()
        return c

    @staticmethod
    def create_sub_category(sub):
        db().categories.update(
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
    def update_category(category):
        CategoryModel.objects(id=category['_id']['$oid']).update(**{
            "set__categoryType": category['categoryType'],
            "set__categoryName": category['categoryName'],
            "set__categoryDescription": category['categoryDescription'],
            "set__active": category.get('active', 0),
        })

    @staticmethod
    def update_sub_category(sub):
        CategoryModel.objects(id=sub['_id'], subCategories__sub_id=sub['sub_id']['$oid']).update(**{
            "set__subCategories__S__subCategoryName": sub['subCategoryName'],
            "set__subCategories__S__subCategoryDescription": sub['subCategoryDescription'],
            "set__subCategories__S__active": sub.get('active', 0),
        })

    @staticmethod
    def delete_category(catalog):
        CategoryModel.objects(id=catalog['_id']['$oid']).delete()

    @staticmethod
    def delete_sub_category(sub):
        db().categories.update(
            {"_id": ObjectId(sub['_id'])},
            {'$pull': {
                'subCategories': {
                    "sub_id": ObjectId(sub['sub_id']['$oid']),
                }
            }}
        )

    @staticmethod
    def update_category_position(data):
        for i, item in enumerate(data):
            CategoryModel.objects(id=item['_id']['$oid']).update_one(set__position=i + 1)
        return CategoryModel.objects().to_json()

    @staticmethod
    def bulk_activate_categories(data):
        for i, item in enumerate(data):
            CategoryModel.objects(id=item['_id']['$oid']).update_one(set__active=1)

    @staticmethod
    def bulk_deactivate_categories(data):
        for i, item in enumerate(data):
            CategoryModel.objects(id=item['_id']['$oid']).update_one(set__active=0)

    @staticmethod
    def bulk_delete_categories(data):
        for i, item in enumerate(data):
            CategoryModel.objects(id=item['_id']['$oid']).delete()

    @staticmethod
    def update_sub_category_position(data):
        for i, item in enumerate(data):
            CategoryModel.objects(id=item['_id']['$oid']).update_one(set__position=i + 1)
        return CategoryModel.objects().to_json()

    @staticmethod
    def bulk_sub_activate_categories(data):
        for i, item in enumerate(data):
            CategoryModel.objects(id=item['_id']['$oid']).update_one(set__active=1)

    @staticmethod
    def bulk_sub_deactivate_categories(data):
        for i, item in enumerate(data):
            CategoryModel.objects(id=item['_id']['$oid']).update_one(set__active=0)

    @staticmethod
    def bulk_sub_delete_categories(data):
        for i, item in enumerate(data):
            CategoryModel.objects(id=item['_id']['$oid']).delete()
