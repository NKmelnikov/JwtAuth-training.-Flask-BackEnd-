import datetime
import mongoengine


class TodoModel(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    text = mongoengine.StringField()
    user_owner_id = mongoengine.ObjectIdField

    meta = {
        'db_alias': 'core',
        'collection': 'todo'
    }