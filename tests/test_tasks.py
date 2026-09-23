import pytest
import json
from app import create_app, db
from flask_jwt_extended import create_access_token
from app.models.users import User


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "sua_chave_secreta"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def token(app):
    """Gera um token válido usando a biblioteca do projeto"""
    with app.app_context():
        user = User(username="gabriela_test", password="123", name="Gabriela", email="gab@test.com")
        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity=str(user.id))
        return access_token



def test_listar_tarefas_vazia(client, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get('/tasks/', headers=headers)

    assert response.status_code == 200
    data = response.get_json()

    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 0


def test_criar_e_deletar_tarefa(client, token):
    headers = {'Authorization': f'Bearer {token}'}

    # 1. Criar tarefa
    payload = {"titulo": "Tarefa de Teste", "descricao": "Testando o Pytest"}
    res_post = client.post('/tasks/', data=json.dumps(payload), headers=headers, content_type='application/json')
    assert res_post.status_code in [200, 201]

    res_del = client.delete('/tasks/1', headers=headers)
    assert res_del.status_code == 200


def test_erro_token_ausente(client):
    response = client.get('/tasks/')
    assert response.status_code == 401