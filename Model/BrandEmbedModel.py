import datetime
import mongoengine


class BrandEmbedModel(mongoengine.EmbeddedDocument):
    _id = mongoengine.StringField()
    createdAt = mongoengine.IntField()
    position = mongoengine.IntField()
    active = mongoengine.IntField()
    brandImgPath = mongoengine.StringField()
    brandName = mongoengine.StringField()

