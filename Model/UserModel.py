import datetime
import mongoengine as m
from ..Model.PersonalModel import PersonalModel


class UserModel(m.Document):
    registered_date = m.DateTimeField(default=datetime.datetime.now)
    email = m.StringField(required=True)
    password = m.StringField(required=True)

    personal = m.EmbeddedDocumentListField(PersonalModel)

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
