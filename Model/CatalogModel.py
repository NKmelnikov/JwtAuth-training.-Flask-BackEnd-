import datetime
import mongoengine


class CatalogModel(mongoengine.Document):
    createdAt = mongoengine.DateTimeField(default=datetime.datetime.now)
    position = mongoengine.IntField(default=1)
    active = mongoengine.IntField(default=1)
    brandId = mongoengine.StringField()
    catalogPdfPath = mongoengine.StringField()
    catalogName = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'catalogs'
    }
