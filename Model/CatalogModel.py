import datetime
import mongoengine as m
from ..Model.BrandModel import BrandModel


class CatalogModel(m.Document):
    brand = m.ReferenceField(BrandModel)
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    catalogPdfPath = m.StringField()
    catalogName = m.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'catalogs'
    }
