from flask import request
from app import db
from ..models.tasks import Tasks, task_schema, tasks_schema

def post_task(current_user):
    data = request.json
    try:
        new_task = Tasks(
            titulo=data['titulo'],
            descricao=data.get('descricao', ''),
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        return {'message': 'Tarefa criada', 'data': task_schema.dump(new_task)}, 201
    except Exception as e:
        db.session.rollback()
        return {'message': 'Erro', 'error': str(e)}, 500

def get_tasks(current_user):
    user_tasks = Tasks.query.filter_by(user_id=current_user.id).all()
    return {'message': 'success', 'data': tasks_schema.dump(user_tasks)}, 200

def update_task(current_user, id):
    task = Tasks.query.filter_by(id=id, user_id=current_user.id).first()

    if not task:
        return {'message': 'Tarefa não encontrada ou acesso negado'}, 404

    try:
        data = request.json
        task.titulo = data.get('titulo', task.titulo)
        task.descricao = data.get('descricao', task.descricao)
        task.status = data.get('status', task.status)

        db.session.commit()
        return {'message': 'Tarefa atualizada', 'data': task_schema.dump(task)}, 200
    except Exception as e:
        db.session.rollback()
        return {'message': 'Erro ao atualizar', 'error': str(e)}, 500

def delete_task(current_user, id):
    task = Tasks.query.filter_by(id=id, user_id=current_user.id).first()

    if not task:
        return {'message': 'Tarefa não encontrada'}, 404

    try:
        db.session.delete(task)
        db.session.commit()
        return {'message': 'Tarefa removida com sucesso!'}, 200
    except Exception as e:
        db.session.rollback()
        return {'message': 'Erro ao deletar', 'error': str(e)}, 500