import datetime
import mongoengine as m
from bson import ObjectId
from ..Model.SubCategoryOilModel import SubCategoryOilModel
from ..Model.CategoryOilModel import CategoryOilModel
from ..Model.BrandModel import BrandModel


class ProductOilModel(m.Document):
    createdAt = m.IntField()
    position = m.IntField()
    active = m.IntField()
    productName = m.StringField()
    productImgPath = m.StringField()
    productDescription = m.StringField()
    productSpec = m.StringField()
    category_id = m.ReferenceField(CategoryOilModel)
    subCategory_id = m.ReferenceField(SubCategoryOilModel)
    brand_id = m.ReferenceField(BrandModel)


