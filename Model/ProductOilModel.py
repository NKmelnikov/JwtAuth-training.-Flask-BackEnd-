import mongoengine as m
import datetime
from ..Model.CategoryModel import CategoryModel
from ..Model.BrandModel import BrandModel


class ProductOilModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    brand_id = m.ReferenceField(BrandModel)
    category_id = m.ReferenceField(CategoryModel)
    subCategory_id = m.ObjectIdField()
    position = m.IntField()
    active = m.IntField()
    slug = m.StringField(unique=True)
    name = m.StringField()
    description = m.StringField()
    spec = m.StringField()
    imgPath = m.StringField()
    pdf1Path = m.StringField()
    pdf2Path = m.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'products_oil'
    }


