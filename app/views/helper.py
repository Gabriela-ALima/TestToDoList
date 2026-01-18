from functools import wraps
from flask import request, jsonify, current_app
import jwt
from werkzeug.security import check_password_hash
import datetime

from .users import user_by_username
from ..models.users import Users


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing', 'data': {}}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = user_by_username(username=data['username'])
        except Exception as e:
            return jsonify({'message': 'Token is invalid or expired', 'data': {}}), 401

        return f(current_user, *args, **kwargs)

    return decorated


def auth():
    auth_data = request.authorization

    if not auth_data or not auth_data.username or not auth_data.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login Required"'}), 401

    user = user_by_username(auth_data.username)

    if not user:
        return jsonify({'message': 'user not found', 'data': {}}), 401

    if check_password_hash(user.password, auth_data.password):
        token = jwt.encode({
            'username': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
        }, current_app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'message': 'Validated successfully', 'token': token}), 200

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login Required"'}), 401