import json
from ..Service.CategoryService import CategoryService


class CategoryController:

    @staticmethod
    def get_categories_oil():
        return CategoryService().get_categories_oil()

    @staticmethod
    def create_category_oil(category):
        CategoryService().create_category_oil(category)
        # CategoryService().update_category_position(json.loads(CategoryService().get_categories_sorted_by_date()))

    @staticmethod
    def create_sub_category_oil(sub):
        CategoryService().create_sub_category_oil(sub)

    @staticmethod
    def update_category_oil(category):
        CategoryService().update_category_oil(category)

    @staticmethod
    def update_sub_category_oil(sub):
        CategoryService().update_sub_category_oil(sub)

    @staticmethod
    def delete_category_oil(category):
        CategoryService().delete_category(category)

    @staticmethod
    def delete_sub_category_oil(sub):
        CategoryService().delete_sub_category(sub)

    @staticmethod
    def update_category_position_oil(data):
        return CategoryService().update_category_position(data)

    @staticmethod
    def bulk_activate_categories_oil(data):
        CategoryService().bulk_activate_categorys(data)
        CategoryService().update_category_position(json.loads(CategoryService().get_categories()))

    @staticmethod
    def bulk_deactivate_categories_oil(data):
        CategoryService().bulk_deactivate_categorys(data)
        CategoryService().update_category_position(json.loads(CategoryService().get_categories()))

    @staticmethod
    def bulk_delete_categories_oil(data):
        CategoryService().bulk_delete_categorys(data)
        CategoryService().update_category_position(json.loads(CategoryService().get_categories()))
