import datetime
import mongoengine
from ..Model.PersonalModel import PersonalModel


class UserModel(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    email = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True)

    personal = mongoengine.EmbeddedDocumentListField(PersonalModel)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }

    @classmethod
    def lookup(cls, email):
        return cls.objects(email=email).first()

    @classmethod
    def identify(cls, id):
        return cls.objects(email=id).first()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.email
