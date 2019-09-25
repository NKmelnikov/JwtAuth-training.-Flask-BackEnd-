from ..Service.UserService import UserService


class UserController:

    @staticmethod
    def create_account(email, password):
        UserService().create_account(email, password)

    @staticmethod
    def create_auth_token(email, password):
        return UserService().create_auth_token(email, password)
