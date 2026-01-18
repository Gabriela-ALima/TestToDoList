from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    # AJUSTE AQUI: Importe os arquivos de model
    # Importar o tasks antes ajuda o Users a achar a referência 'Tasks'
    from .models import tasks, users

    with app.app_context():
        # O db.create_all() agora sabe quem é Users e quem é Tasks
        db.create_all()

    from .routes.routes import routes
    app.register_blueprint(routes)

    return app


