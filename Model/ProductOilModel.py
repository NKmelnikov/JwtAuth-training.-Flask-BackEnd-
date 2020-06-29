import mongoengine as m
from ..Model.SubCategoryModel import SubCategoryModel
from ..Model.CategoryModel import CategoryModel
from ..Model.BrandModel import BrandModel


class ProductOilModel(m.Document):
    createdAt = m.IntField()
    position = m.IntField()
    active = m.IntField()
    productName = m.StringField()
    productDescription = m.StringField()
    productSpec = m.StringField()
    productImgPath = m.StringField()
    category_id = m.ReferenceField(CategoryModel)
    subCategory_id = m.ReferenceField(SubCategoryModel)
    brand_id = m.ReferenceField(BrandModel)


