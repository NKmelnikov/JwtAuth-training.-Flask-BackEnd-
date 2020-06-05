import datetime
import mongoengine
from ..Model.BrandModel import BrandModel


class CatalogModel(mongoengine.Document):
    createdAt = mongoengine.DateTimeField(default=datetime.datetime.now)
    position = mongoengine.IntField(default=1)
    active = mongoengine.IntField(default=1)
    catalogPdfPath = mongoengine.StringField()
    catalogName = mongoengine.StringField()
    brand = mongoengine.ReferenceField(BrandModel)

    meta = {
        'db_alias': 'core',
        'collection': 'catalogs'
    }
