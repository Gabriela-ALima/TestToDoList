import datetime
from app import db, ma

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    tasks = db.relationship("Tasks", backref="owner", lazy=True)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        exclude = ("password",)

    tasks = ma.Nested("TasksSchema", many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


