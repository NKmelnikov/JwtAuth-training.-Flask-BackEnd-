from ..Model.PostModel import PostModel
from .Service import Service


class PostService(Service):

    @staticmethod
    def create_post(post) -> PostModel:
        p = PostModel()
        p.position = 0
        p.postTitle = post['postTitle']
        p.postShortText = post['postShortText']
        p.postArticle = post['postArticle']
        p.postImgPath = post['postImgPath']
        p.active = post.get('active', 1)
        p.save()
        return p

    @staticmethod
    def update_post(post):
        PostModel.objects(id=post['_id']['$oid']).update(**{
            "set__postTitle": post['postTitle'],
            "set__postShortText": post['postShortText'],
            "set__postArticle": post['postArticle'],
            "set__postImgPath": post['postImgPath'],
            "set__active": post.get('active', 1),
        })
