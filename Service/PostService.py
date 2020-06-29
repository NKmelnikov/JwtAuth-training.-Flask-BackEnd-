from ..Model.PostModel import PostModel
from .Service import Service


class PostService(Service):

    @staticmethod
    def create_post(_post) -> PostModel:
        post = PostModel()
        post.position = 0
        post.postTitle = _post['postTitle']
        post.postShortText = _post['postShortText']
        post.postArticle = _post['postArticle']
        post.postImgPath = _post['postImgPath']
        post.active = _post.get('active', 0)
        post.save()
        return post

    @staticmethod
    def update_post(post):
        PostModel.objects(id=post['_id']['$oid']).update(**{
            "set__postTitle": post['postTitle'],
            "set__postShortText": post['postShortText'],
            "set__postArticle": post['postArticle'],
            "set__postImgPath": post['postImgPath'],
            "set__active": post.get('active', 0),
        })
