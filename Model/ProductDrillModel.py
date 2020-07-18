import mongoengine as m
import datetime
from ..Model.CategoryModel import CategoryModel
from ..Model.BrandModel import BrandModel


class ProductDrillModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    brand_id = m.ReferenceField(BrandModel)
    category_id = m.ReferenceField(CategoryModel)
    subCategory_id = m.ObjectIdField()
    position = m.IntField()
    active = m.IntField()
    productSlug = m.StringField(unique=True)
    productName = m.StringField()
    productDescription = m.StringField()
    productPdfPath = m.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'products_drill'
    }


