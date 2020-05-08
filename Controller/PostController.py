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

    @staticmethod
    def bulk_activate(data):
        PostService().bulk_activate(data)

    @staticmethod
    def bulk_deactivate(data):
        PostService().bulk_deactivate(data)

    @staticmethod
    def bulk_delete(data):
        PostService().bulk_delete(data)


