from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema


def post_user():
    try:
        data = request.json
        user = Users(
            username=data['username'],
            password=generate_password_hash(data['password']),
            name=data['name'],
            email=data['email']
        )

        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user)
        return jsonify({'message': 'success', 'data': result}), 201

    except Exception as e:
        db.session.rollback()
        print("<<<<< ERRO DETALHADO ABAIXO >>>>>")
        print(e)
        return jsonify({'message': 'fail', 'error': str(e)}), 500


def update_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'Usuário não encontrado', 'data': {}}), 404

    try:
        data = request.json

        user.username = data.get('username', user.username)
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)

        if 'password' in data:
            user.password = generate_password_hash(data['password'])

        db.session.commit()

        result = user_schema.dump(user)
        return jsonify({'message': 'success', 'data': result}), 200

    except Exception as e:
        db.session.rollback()
        print("<<<<< ERRO NO UPDATE >>>>>")
        print(e)
        return jsonify({'message': 'fail', 'error': str(e)}), 500

def get_users():
    try:
        users = Users.query.all()

        result = users_schema.dump(users)

        return jsonify({'message': 'success', 'data': result}), 200

    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
        return jsonify({'message': 'fail', 'error': str(e)}), 500


def get_user(id):
    try:

        user = Users.query.get(id)


        if not user:
            return jsonify({'message': 'fail', 'error': 'Usuário não encontrado'}), 404


        result = user_schema.dump(user)

        return jsonify({'message': 'success', 'data': result}), 200

    except Exception as e:
        print(f"Erro detectado: {e}")
        return jsonify({'message': 'fail', 'error': str(e)}), 500


def delete_user(id):

    user = Users.query.get(id)


    if not user:
        return jsonify({'message': 'Usuário não encontrado', 'data': {}}), 404

    try:

        db.session.delete(user)
        db.session.commit()


        result = user_schema.dump(user)
        return jsonify({'message': 'success', 'data': result}), 200

    except Exception as e:
        db.session.rollback()
        print(f"Erro ao eliminar: {e}")
        return jsonify({'message': 'fail', 'error': str(e)}), 500


def user_by_username(username):
    try:
        return Users.query.filter_by(username=username).first()
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
        return None