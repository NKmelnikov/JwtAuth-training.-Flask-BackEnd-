import datetime
import mongoengine


class PostModel(mongoengine.Document):
    createdAt = mongoengine.DateTimeField(default=datetime.datetime.now)
    position = mongoengine.IntField(default=1)
    active = mongoengine.IntField(default=1)
    postImgPath = mongoengine.StringField()
    postTitle = mongoengine.StringField()
    postShortText = mongoengine.StringField()
    postArticle = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'posts'
    }
