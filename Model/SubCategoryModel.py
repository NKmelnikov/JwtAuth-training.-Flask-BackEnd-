import datetime
import mongoengine as m
from bson import ObjectId


class SubCategoryModel(m.EmbeddedDocument):
    sub_id = m.ObjectIdField(default=ObjectId)
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    name = m.StringField()
    description = m.StringField()

