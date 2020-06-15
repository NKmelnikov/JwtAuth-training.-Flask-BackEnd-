import datetime
import mongoengine as m


class TodoModel(m.Document):
    registered_date = m.DateTimeField(default=datetime.datetime.now)
    text = m.StringField()
    user_owner_id = m.ObjectIdField

    meta = {
        'db_alias': 'core',
        'collection': 'todo'
    }
