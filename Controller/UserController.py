from ..Infrastructure import state
from ..Service.UserService import UserService


class UserController:

    @staticmethod
    def create_account(name):
        state.active_account = UserService().create_account(name)
