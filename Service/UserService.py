from flask import jsonify
from ..Model.UserModel import UserModel
from ..Config.auth import guard


class UserService:

    @staticmethod
    def create_account(email, password) -> UserModel:
        user = UserModel()
        user.email = email
        user.password = guard.hash_password(password)
        user.save()
        return user

    @staticmethod
    def create_auth_token(email, password) -> UserModel:
        user = guard.authenticate(email, password)
        token = guard.encode_jwt_token(user)
        return jsonify({'email': email, 'password': password, 'token': token})
