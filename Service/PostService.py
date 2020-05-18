from flask import jsonify
from bson import json_util
from ..Model.PostModel import PostModel


class PostService:

    @staticmethod
    def get_posts() -> PostModel:
        return PostModel.objects().order_by('position').to_json()

    @staticmethod
    def get_posts_sorted_by_date() -> PostModel:
        return PostModel.objects().order_by('-createdAt').to_json()

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

    @staticmethod
    def delete_post(post):
        PostModel.objects(id=post['_id']['$oid']).delete()

    @staticmethod
    def update_post_position(data):
        for i, item in enumerate(data):
            PostModel.objects(id=item['_id']['$oid']).update_one(set__position=i + 1)
        return PostModel.objects().to_json()

    @staticmethod
    def bulk_activate_posts(data):
        for i, item in enumerate(data):
            PostModel.objects(id=item['_id']['$oid']).update_one(set__active=1)

    @staticmethod
    def bulk_deactivate_posts(data):
        for i, item in enumerate(data):
            PostModel.objects(id=item['_id']['$oid']).update_one(set__active=0)

    @staticmethod
    def bulk_delete_posts(data):
        for i, item in enumerate(data):
            PostModel.objects(id=item['_id']['$oid']).delete()
