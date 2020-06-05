import datetime
import mongoengine
from ..Model.ProductOilModel import ProductOilModel


class CategoryOilModel(mongoengine.Document):
    createdAt = mongoengine.DateTimeField(default=datetime.datetime.now)
    position = mongoengine.IntField(default=1)
    active = mongoengine.IntField(default=1)
    categoryName = mongoengine.StringField()
    categoryDescription = mongoengine.StringField()
    products = mongoengine.EmbeddedDocumentListField(ProductOilModel)

    meta = {
        'db_alias': 'core',
        'collection': 'categories_oil'
    }
