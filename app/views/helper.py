from flask import request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.models.users import User

def auth():
    """
    Função de autenticação corrigida para Flask-RestX.
    Retorna dicionários puros em vez de jsonify.
    """
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return {
            "message": "Dados insuficientes",
            "error": "username e password são obrigatórios"
        }, 400

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user:
        return {"message": "Usuário não encontrado"}, 404

    if check_password_hash(user.password, password):
        access_token = create_access_token(identity=str(user.id))

        return {
            "message": "Login realizado com sucesso",
            "access_token": access_token
        }, 200

    return {"message": "Senha incorreta"}, 401