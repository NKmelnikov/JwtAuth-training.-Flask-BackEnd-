import mongoengine


class PersonalModel(mongoengine.EmbeddedDocument):
    user_owner_id = mongoengine.ObjectIdField
    gender = mongoengine.StringField()
    age = mongoengine.StringField()
    phone = mongoengine.IntField()
    email = mongoengine.EmailField()
