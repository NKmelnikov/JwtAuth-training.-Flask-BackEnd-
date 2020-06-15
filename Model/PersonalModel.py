import mongoengine as m


class PersonalModel(m.EmbeddedDocument):
    user_owner_id = m.ObjectIdField
    gender = m.StringField()
    age = m.StringField()
    phone = m.IntField()
    email = m.EmailField()
