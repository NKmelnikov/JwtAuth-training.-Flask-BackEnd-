from flask import Blueprint, request, Response, make_response, jsonify
from flask_praetorian import auth_required

from ..Config.auth import guard
authenticated = Blueprint('authenticated', __name__)

@authenticated.route('/home')
@auth_required
def protected():
    return jsonify({'result': 'You are in a special area!'})


