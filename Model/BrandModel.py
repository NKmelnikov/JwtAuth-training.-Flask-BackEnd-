import datetime
import mongoengine as m


class BrandModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    imgPath = m.StringField()
    slug = m.StringField(unique=True)
    name = m.StringField()
    description = m.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'brands'
    }
