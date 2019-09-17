from typing import List, Optional
import datetime
import bson
from ..Model.UserModel import UserModel


class UserService:

    @staticmethod
    def create_account(name) -> UserModel:
        user = UserModel()
        user.name = name
        user.save()
        return user

    @staticmethod
    def find_account_by_name(name) -> UserModel:
        user = UserModel.objects(name=name).first()
        return user
