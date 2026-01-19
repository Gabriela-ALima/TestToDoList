from werkzeug.security import generate_password_hash
from app import db
from flask import request
from ..models.users import User, user_schema, users_schema

def post_user():
    try:
        data = request.json
        user = User(
            username=data['username'],
            password=generate_password_hash(data['password']),
            name=data['name'],
            email=data['email']
        )

        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user)
        return {'message': 'success', 'data': result}, 201

    except Exception as e:
        db.session.rollback()
        return {'message': 'fail', 'error': str(e)}, 500


def update_user(id):
    user = User.query.get(id)

    if not user:
        return {'message': 'Usuário não encontrado', 'data': {}}, 404

    try:
        data = request.json
        user.username = data.get('username', user.username)
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)

        if 'password' in data:
            user.password = generate_password_hash(data['password'])

        db.session.commit()
        result = user_schema.dump(user)
        return {'message': 'success', 'data': result}, 200

    except Exception as e:
        db.session.rollback()
        return {'message': 'fail', 'error': str(e)}, 500

def get_users():
    try:
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return {'message': 'success', 'data': result}, 200
    except Exception as e:
        return {'message': 'fail', 'error': str(e)}, 500


def get_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return {'message': 'fail', 'error': 'Usuário não encontrado'}, 404

        result = user_schema.dump(user)
        return {'message': 'success', 'data': result}, 200
    except Exception as e:
        return {'message': 'fail', 'error': str(e)}, 500


def delete_user(id):
    user = User.query.get(id)
    if not user:
        return {'message': 'Usuário não encontrado', 'data': {}}, 404

    try:
        db.session.delete(user)
        db.session.commit()
        result = user_schema.dump(user)
        return {'message': 'success', 'data': result}, 200
    except Exception as e:
        db.session.rollback()
        return {'message': 'fail', 'error': str(e)}, 500


def user_by_username(username):
    try:
        return User.query.filter_by(username=username).first()
    except Exception as e:
        return None