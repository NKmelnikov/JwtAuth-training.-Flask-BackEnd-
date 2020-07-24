import datetime
import mongoengine as m
from ..Model.SubCategoryModel import SubCategoryModel


class CategoryModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    type = m.IntField(default=1)  # 1 = Oil, 2 = Drill
    name = m.StringField()
    description = m.StringField()
    subCategories = m.EmbeddedDocumentListField(SubCategoryModel)

    meta = {
        'db_alias': 'core',
        'collection': 'categories'
    }
