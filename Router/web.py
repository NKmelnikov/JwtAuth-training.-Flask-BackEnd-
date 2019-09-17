from flask import Blueprint, request, escape
from ..Controller.UserController import UserController

web = Blueprint('app', __name__)


@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        UserController().create_account(name)
        return 'User registered'
