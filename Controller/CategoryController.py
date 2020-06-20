import json
from ..Service.CategoryService import CategoryService


class CategoryController:

    @staticmethod
    def get_categories():
        return CategoryService().get_categories()

    @staticmethod
    def get_category_by_id(category_id):
        return CategoryService().get_category_by_id(category_id, 'position', 1)

    @staticmethod
    def create_category(category):
        CategoryService().create_category(category)
        CategoryService().update_category_position(json.loads(CategoryService().get_categories_sorted_by_date()))

    @staticmethod
    def update_category(category):
        CategoryService().update_category(category)

    @staticmethod
    def delete_category(category):
        CategoryService().delete_category(category)

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

    @staticmethod
    def create_sub_category(sub):
        CategoryService().create_sub_category(sub)
        CategoryService().update_sub_category_position(
            json.loads(CategoryService().get_category_by_id(sub, 'createdAt', -1)))

    @staticmethod
    def update_sub_category(sub):
        CategoryService().update_sub_category(sub)

    @staticmethod
    def delete_sub_category(sub):
        CategoryService().delete_sub_category(sub)

    @staticmethod
    def update_sub_category_position(data):
        return CategoryService().update_sub_category_position(data)

    @staticmethod
    def bulk_activate_sub_categories(data):
        category_id = {'id': data[-1]}
        CategoryService().bulk_activate_sub_categories(data)
        CategoryService().update_sub_category_position(json.loads(
            CategoryService().get_category_by_id(category_id, 'position', 1)))

    @staticmethod
    def bulk_deactivate_sub_categories(data):
        category_id = {'id': data[-1]}
        CategoryService().bulk_deactivate_sub_categories(data)
        CategoryService().update_sub_category_position(json.loads(
            CategoryService().get_category_by_id(category_id, 'position', 1)))

    @staticmethod
    def bulk_delete_sub_categories(data):
        category_id = {'id': data[-1]}
        CategoryService().bulk_delete_sub_categories(data)
        CategoryService().update_sub_category_position(json.loads(
            CategoryService().get_category_by_id(category_id, 'position', 1)))
