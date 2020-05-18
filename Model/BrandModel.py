import datetime
import mongoengine


class BrandModel(mongoengine.Document):
    createdAt = mongoengine.DateTimeField(default=datetime.datetime.now)
    position = mongoengine.IntField(default=1)
    active = mongoengine.IntField(default=1)
    brandImgPath = mongoengine.StringField()
    brandName = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'brands'
    }
