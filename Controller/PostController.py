from ..Service.PostService import PostService
import json

class PostController:

    @staticmethod
    def get_posts():
        return PostService().get_posts()

    @staticmethod
    def create_post(post):
        PostService().create_post(post)
        PostService().update_post_position(json.loads(PostService().get_posts_sorted_by_date()))

    @staticmethod
    def update_post(post):
        PostService().update_post(post)

    @staticmethod
    def delete_post(post):
        PostService().delete_post(post)

    @staticmethod
    def update_post_position(data):
        return PostService().update_post_position(data)

    @staticmethod
    def bulk_activate(data):
        PostService().bulk_activate(data)
        PostService().update_post_position(json.loads(PostService().get_posts()))


    @staticmethod
    def bulk_deactivate(data):
        PostService().bulk_deactivate(data)
        PostService().update_post_position(json.loads(PostService().get_posts()))


    @staticmethod
    def bulk_delete(data):
        PostService().bulk_delete(data)
        PostService().update_post_position(json.loads(PostService().get_posts()))



