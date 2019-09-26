from flask import Blueprint, request, Response, make_response, jsonify
from flask_praetorian import auth_required
from flask_praetorian.exceptions import (
    AuthenticationError,
    BlacklistedError,
    ClaimCollisionError,
    EarlyRefreshError,
    ExpiredAccessError,
    ExpiredRefreshError,
    InvalidRegistrationToken,
    InvalidTokenHeader,
    InvalidUserError,
    LegacyScheme,
    MissingClaimError,
    MissingTokenHeader,
    MissingUserError,
    MisusedRegistrationToken,
    ConfigurationError,
    PraetorianError,
)
from ..Config.auth import guard
authenticated = Blueprint('authenticated', __name__)


@auth_required
def auth_check():
    return jsonify({'result': 'OK'})


def auth_middleware():
    print('---------------1')
    try:
        auth_check()
    except ExpiredAccessError:
        print('token experied')
        token = guard.read_token_from_header()
        n = guard.refresh_jwt_token(token)
        print(n)
        res = make_response('token_will_be_refreshed')
        res.headers['Bearer'] = jsonify({'access_token': n})
        protected()
    print('---------------2')


@authenticated.route('/protected')
@auth_required
def protected():
    return jsonify({'result': 'You are in a special area!'})


