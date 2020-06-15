import datetime
import mongoengine as m
from ..Model.SubCategoryOilModel import SubCategoryOilModel


class CategoryOilModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    categoryName = m.StringField()
    categoryDescription = m.StringField()
    subCategories = m.EmbeddedDocumentListField(SubCategoryOilModel)

    meta = {
        'db_alias': 'core',
        'collection': 'categories_oil'
    }
