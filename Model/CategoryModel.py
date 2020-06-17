import datetime
import mongoengine as m
from ..Model.SubCategoryModel import SubCategoryModel


class CategoryModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    categoryType = m.IntField(default=1)  # 1 = Oil, 2 = Drill
    categoryName = m.StringField()
    categoryDescription = m.StringField()
    subCategories = m.EmbeddedDocumentListField(SubCategoryModel)

    meta = {
        'db_alias': 'core',
        'collection': 'categories_oil'
    }
