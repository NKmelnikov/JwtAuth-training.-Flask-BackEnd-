import datetime
import mongoengine as m
from bson import ObjectId


class SubCategoryOilModel(m.EmbeddedDocument):
    _id = m.ObjectIdField(default=ObjectId)
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    subCategoryName = m.StringField()
    subCategoryDescription = m.StringField()

