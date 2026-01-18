from flask import Blueprint, jsonify

from app.views.users import post_user, update_user, get_users, get_user, delete_user


routes = Blueprint('main_routes', __name__)

@routes.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'API To-Do List Online!'})


@routes.route('/users', methods=['POST'])
def create_user():
    return post_user()


@routes.route('/users/<int:id>', methods=['PUT'])
def edit_user(id):
    return update_user(id)


@routes.route('/users', methods=['GET'])
def list_users():
    return get_users()



@routes.route('/users/<int:id>', methods=['GET'])
def search_one_user(id):
    return get_user(id)


@routes.route('/users/<int:id>', methods=['DELETE'])
def remove_user(id):
    return delete_user(id)

