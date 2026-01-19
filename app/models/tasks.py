import datetime
from app import db, ma

class Tasks(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    status = db.Column(db.Boolean, default=False)
    data_criacao = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

class TasksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tasks
        load_instance = True
        sqla_session = db.session
        include_fk = True

task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)