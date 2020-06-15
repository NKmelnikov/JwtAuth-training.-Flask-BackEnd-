import datetime
import mongoengine as m


class PostModel(m.Document):
    createdAt = m.DateTimeField(default=datetime.datetime.now)
    position = m.IntField(default=1)
    active = m.IntField(default=1)
    postImgPath = m.StringField()
    postTitle = m.StringField()
    postShortText = m.StringField()
    postArticle = m.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'posts'
    }
