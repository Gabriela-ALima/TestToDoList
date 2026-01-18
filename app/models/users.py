import datetime
from app import db, ma

"""Definição da classe/tabela dos usuários e seus campos"""
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now)


    tasks = db.relationship('Tasks', backref='author', lazy=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

"""Definindo o schema do Marshmallow para facilitar a utilização de json"""
class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True
        sqla_session = db.session
        include_relationships = True

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)



