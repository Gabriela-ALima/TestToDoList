from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.views import users, tasks, helper
from app.models.users import User


login_ns = Namespace("login", description="Operações de Acesso/Autenticação")
user_ns = Namespace("users", description="Gerenciamento de Usuários")
task_ns = Namespace("tasks", description="Gerenciamento de Tarefas")



login_model = login_ns.model('Login', {
    'username': fields.String(required=True, example='joao_dev'),
    'password': fields.String(required=True, example='123456')
})

user_model = user_ns.model('User', {
    'username': fields.String(required=True, example='joao_dev'),
    'password': fields.String(required=True, example='123456'),
    'name': fields.String(required=True, example='João Silva'),
    'email': fields.String(required=True, example='joao@email.com')
})

task_model = task_ns.model('Task', {
    'titulo': fields.String(required=True, example='Estudar Python'),
    'descricao': fields.String(example='Finalizar o projeto ToDo List'),
    'status': fields.Boolean(default=False)
})

@login_ns.route("/")
class Login(Resource):
    @login_ns.expect(login_model)
    def post(self):
        """Faz login e gera o token JWT"""
        return helper.auth()

@user_ns.route("/")
class UserList(Resource):
    @jwt_required()
    @user_ns.doc(security="Bearer")
    def get(self):
        """Listar todos os usuários (Requer Token)"""
        return users.get_users()

    @user_ns.expect(user_model)
    def post(self):
        """Criar um novo usuário (Público)"""
        return users.post_user()

@user_ns.route("/<int:id>")
class UserDetail(Resource):
    @jwt_required()
    @user_ns.doc(security="Bearer")
    def get(self, id):
        """Buscar usuário por ID"""
        return users.get_user(id)

    @jwt_required()
    @user_ns.doc(security="Bearer")
    @user_ns.expect(user_model)
    def put(self, id):
        """Atualizar um usuário"""
        return users.update_user(id)

    @jwt_required()
    @user_ns.doc(security="Bearer")
    def delete(self, id):
        """Deletar um usuário"""
        return users.delete_user(id)

@task_ns.route("/")
class TaskList(Resource):
    @jwt_required()
    @task_ns.doc(security="Bearer")
    def get(self):
        """Listar tarefas do usuário logado"""
        user_id = get_jwt_identity()
        current_user = User.query.get(user_id)
        return tasks.get_tasks(current_user)

    @jwt_required()
    @task_ns.doc(security="Bearer")
    @task_ns.expect(task_model)
    def post(self):
        """Criar uma nova tarefa"""
        user_id = get_jwt_identity()
        current_user = User.query.get(user_id)
        return tasks.post_task(current_user)

@task_ns.route("/<int:id>")
class TaskDetail(Resource):
    @jwt_required()
    @task_ns.doc(security="Bearer")
    @task_ns.expect(task_model)
    def put(self, id):
        """Atualizar uma tarefa"""
        user_id = get_jwt_identity()
        current_user = User.query.get(user_id)
        return tasks.update_task(current_user, id)

    @jwt_required()
    @task_ns.doc(security="Bearer")
    def delete(self, id):
        """Deletar uma tarefa"""
        user_id = get_jwt_identity()
        current_user = User.query.get(user_id)
        return tasks.delete_task(current_user, id)