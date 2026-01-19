from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    authorizations = {
        "Bearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Digite: Bearer SEU_TOKEN"
        }
    }

    api = Api(
        app,
        title="To-Do List API",
        version="1.0.0",
        description="API com autenticação JWT e CRUD completo",
        authorizations=authorizations,
        security="Bearer",
        doc="/swagger"
    )

    from .models import User, tasks
    with app.app_context():
        db.create_all()

    from .routes.routes import login_ns, user_ns, task_ns

    api.add_namespace(login_ns, path='/usuarios/logar')
    api.add_namespace(user_ns, path='/usuarios')
    api.add_namespace(task_ns, path='/tasks')

    return app