import pytest
from app import create_app, db
from flask_jwt_extended import create_access_token
from app.models.users import User


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": app.config.get("SECRET_KEY", "test-secret-key")
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
    """Gera um token válido usando a biblioteca correta do projeto"""
    with app.app_context():
        user = User.query.filter_by(username="gabriela_test").first()
        if not user:
            user = User(
                username="gabriela_test",
                password="123",  # Lembre-se que se houver hash na view, aqui deve bater
                name="Gabriela",
                email="gab@test.com"
            )
            db.session.add(user)
            db.session.commit()

        access_token = create_access_token(identity=str(user.id))

        return access_token