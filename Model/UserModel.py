import datetime
import mongoengine
from ..Model.PersonalModel import PersonalModel


class UserModel(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    personal = mongoengine.EmbeddedDocumentListField(PersonalModel)

    meta = {
        'db_alias': 'core',
        'collection': 'user'
    }