from flask import jsonify
from bson import json_util
from ..Model.PostModel import PostModel


class PostService:

    @staticmethod
    def get_posts() -> PostModel:
        return PostModel.objects().to_json()

    @staticmethod
    def create_post(_post) -> PostModel:
        post = PostModel()
        post.position = _post['position']
        post.active = _post['active']
        post.postImgPath = _post['postImgPath']
        post.postTitle = _post['postTitle']
        post.postShortText = _post['postShortText']
        post.postArticle = _post['postArticle']
        post.save()
        return post
