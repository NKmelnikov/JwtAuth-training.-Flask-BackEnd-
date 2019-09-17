from typing import Optional

from ..Model.UserModel import UserModel
from ..Service.UserService import UserService

active_account: Optional[UserModel] = None


def reload_account():
    global active_account
    if not active_account:
        return

    active_account = UserService.find_account_by_name()
