import datetime
import mongoengine as m


class BrandModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    brandImgPath = m.StringField()
    brandName = m.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'brands'
    }
