from flask import abort, make_response
from ..db import db


def validate_model(cls, task_id):
    try:
        task_id = int(task_id)
    except:
        response = {"message": f"{cls.__name__} {task_id} invalid"}
        abort(make_response(response, 400))
        
    query = db.select(cls).where(cls.id == task_id)
    task = db.session.scalar(query)

    if not task:
        response = {"message": f"{cls.__name__} {task_id} not found"}
        abort(make_response(response, 404))
    
    return task

