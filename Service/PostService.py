from ..Model.PostModel import PostModel
from .Service import Service


class PostService(Service):

    @staticmethod
    def create_post(post) -> PostModel:
        p = PostModel()
        p.position = 0
        p.title = post['title']
        p.shortText = post['shortText']
        p.article = post['article']
        p.imgPath = post['imgPath']
        p.active = post.get('active', 1)
        p.save()
        return p

    @staticmethod
    def update_post(post):
        PostModel.objects(id=post['_id']['$oid']).update(**{
            "set__title": post['title'],
            "set__shortText": post['shortText'],
            "set__article": post['article'],
            "set__imgPath": post['imgPath'],
            "set__active": post.get('active', 1),
        })
