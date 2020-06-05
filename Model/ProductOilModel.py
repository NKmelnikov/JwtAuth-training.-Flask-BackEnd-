import datetime
import mongoengine as m
from bson import ObjectId
from ..Model.SubCategoryOilModel import SubCategoryOilModel
from ..Model.BrandEmbedModel import BrandEmbedModel


class ProductOilModel(m.EmbeddedDocument):
    _id = m.ObjectIdField(default=ObjectId)
    createdAt = m.IntField()
    position = m.IntField()
    active = m.IntField()
    productName = m.StringField()
    productImgPath = m.StringField()
    productDescription = m.StringField()
    productSpec = m.StringField()
    subCategory = m.EmbeddedDocumentListField(SubCategoryOilModel)
    brand = m.EmbeddedDocumentField(BrandEmbedModel)


