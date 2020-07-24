from bson.json_util import dumps
import datetime
from bson import ObjectId
from ..Model.CategoryModel import CategoryModel
from ..Model.SubCategoryModel import SubCategoryModel
from ..Config.database import db
from .Service import Service


class CategoryService(Service):

    @staticmethod
    def get_category_by_id(category_id, sort_type, direction):

        request = list(db().categories.aggregate([
            {'$match': {'_id': ObjectId(category_id['id'])}},
            {'$unwind': '$subCategories'},
            {'$sort': {f'subCategories.{sort_type}': direction}},
            {'$group': {
                '_id': '$_id',
                'createdAt': {'$first': '$createdAt'},
                'position': {'$first': '$position'},
                'active': {'$first': '$active'},
                'type': {'$first': '$type'},
                'name': {'$first': '$name'},
                'description': {'$first': '$description'},
                'subCategories': {
                    '$push': '$subCategories'
                }
            }
            },
        ]))

        return dumps(request[0]) if len(request) > 0 else CategoryModel.objects().get(id=category_id['id']).to_json()

    @staticmethod
    def create_category(category) -> CategoryModel:
        c = CategoryModel()
        c.position = 0
        c.active = category.get('active', 1)
        c.type = category['type']
        c.name = category['name']
        c.description = category['description']
        c.s = SubCategoryModel()
        c.save()
        return c

    @staticmethod
    def update_category(category):
        CategoryModel.objects(id=category['_id']['$oid']).update(**{
            'set__type': category['type'],
            'set__name': category['name'],
            'set__description': category['description'],
            'set__active': category.get('active', 1),
        })

    # ==================== SUBCATEGORY ====================
    @staticmethod
    def create_sub_category(sub):
        db().categories.update(
            {'_id': ObjectId(sub['id'])},
            {'$push': {
                'subCategories': {
                    'sub_id': ObjectId(),
                    'createdAt': datetime.datetime.now(),
                    'position': sub.get('position', 0),
                    'active': sub.get('active', 1),
                    'name': sub['name'],
                    'description': sub['description']

                }
            }}
        )

    @staticmethod
    def update_sub_category(sub):
        CategoryModel.objects(id=sub['id'], subCategories__sub_id=sub['sub_id']['$oid']).update(**{
            'set__subCategories__S__name': sub['name'],
            'set__subCategories__S__description': sub['description'],
            'set__subCategories__S__active': sub.get('active', 1),
        })

    @staticmethod
    def delete_sub_category(sub):
        db().categories.update(
            {'_id': ObjectId(sub['id'])},
            {'$pull': {
                'subCategories': {
                    'sub_id': ObjectId(sub['sub_id']['$oid']),
                }
            }}
        )

    @staticmethod
    def update_sub_category_position(data):
        category_id = data[-1] if isinstance(data, list) else data['_id']['$oid']
        for i, item in enumerate(data):
            if 'sub_id' in item:
                CategoryModel.objects(id=category_id, subCategories__sub_id=item['sub_id']['$oid']) \
                    .update_one(set__subCategories__S__position=i + 1)
        return CategoryModel.objects().to_json()

    @staticmethod
    def bulk_activate_sub_categories(data):
        category_id = data[-1]
        for i, item in enumerate(data):
            if 'sub_id' in item:
                CategoryModel.objects(id=category_id, subCategories__sub_id=item['sub_id']['$oid']).update_one(
                    set__subCategories__S__active=1)

    @staticmethod
    def bulk_deactivate_sub_categories(data):
        category_id = data[-1]
        for i, item in enumerate(data):
            if 'sub_id' in item:
                CategoryModel.objects(id=category_id, subCategories__sub_id=item['sub_id']['$oid']).update_one(
                    set__subCategories__S__active=0)

    @staticmethod
    def bulk_delete_sub_categories(data):
        for i, item in enumerate(data):
            category_id = data[-1]
            if 'sub_id' in item:
                db().categories.update(
                    {'_id': ObjectId(category_id)},
                    {'$pull': {
                        'subCategories': {
                            'sub_id': ObjectId(item['sub_id']['$oid']),
                        }
                    }}
                )
