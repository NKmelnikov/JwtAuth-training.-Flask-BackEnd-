import json
from ..Service.CategoryService import CategoryService


class CategoryController:

    @staticmethod
    def get_categories():
        return CategoryService().get_categories()

    @staticmethod
    def get_category_by_id(category_id):
        return CategoryService().get_category_by_id(category_id)

    @staticmethod
    def create_category(category):
        CategoryService().create_category(category)
        CategoryService().update_category_position(json.loads(CategoryService().get_categories_sorted_by_date()))

    @staticmethod
    def create_sub_category(sub):
        CategoryService().create_sub_category(sub)

    @staticmethod
    def update_category(category):
        CategoryService().update_category(category)

    @staticmethod
    def update_sub_category(sub):
        CategoryService().update_sub_category(sub)

    @staticmethod
    def delete_category(category):
        CategoryService().delete_category(category)

    @staticmethod
    def delete_sub_category(sub):
        CategoryService().delete_sub_category(sub)

    @staticmethod
    def update_category_position(data):
        return CategoryService().update_category_position(data)

    @staticmethod
    def bulk_activate_categories(data):
        CategoryService().bulk_activate_categories(data)
        CategoryService().update_category_position(json.loads(CategoryService().get_categories()))

    @staticmethod
    def bulk_deactivate_categories(data):
        CategoryService().bulk_deactivate_categories(data)
        CategoryService().update_category_position(json.loads(CategoryService().get_categories()))

    @staticmethod
    def bulk_delete_categories(data):
        CategoryService().bulk_delete_categories(data)
        CategoryService().update_category_position(json.loads(CategoryService().get_categories()))
