from ..Service.PostService import PostService


class PostController:

    @staticmethod
    def get_posts():
        return PostService().get_posts()

    @staticmethod
    def create_post(post):
        PostService().create_post(post)

    @staticmethod
    def update_post(post):
        PostService().update_post(post)

    @staticmethod
    def delete_post(post):
        PostService().delete_post(post)

    @staticmethod
    def update_post_position(data):
        return PostService().update_post_position(data)


