import datetime
import mongoengine as m
from bson import ObjectId


class SubCategoryOilModel(m.EmbeddedDocument):
    _id = m.ObjectIdField(default=ObjectId)
    createdAt = m.IntField()
    position = m.IntField()
    active = m.IntField()
    subCategoryName = m.StringField()

