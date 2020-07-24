import datetime
import mongoengine as m


class PostModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    imgPath = m.StringField()
    title = m.StringField()
    shortText = m.StringField()
    article = m.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'posts'
    }
