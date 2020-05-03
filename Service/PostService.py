from flask import jsonify
from bson import json_util
from ..Model.PostModel import PostModel


class PostService:

    @staticmethod
    def get_posts() -> PostModel:
        return PostModel.objects().order_by('position').to_json()

    @staticmethod
    def create_post(_post) -> PostModel:
        post = PostModel()
        post.position = PostModel.objects().count()+1
        post.active = _post['active']
        post.postImgPath = _post['postImgPath']
        post.postTitle = _post['postTitle']
        post.postShortText = _post['postShortText']
        post.postArticle = _post['postArticle']
        post.save()
        return post

    @staticmethod
    def update_post_position(data):
        for i, item in enumerate(data):
            PostModel.objects(id=item['_id']['$oid']).update_one(set__position=i+1)
        return PostModel.objects().to_json()
