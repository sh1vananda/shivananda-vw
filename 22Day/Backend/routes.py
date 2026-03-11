from flask import Blueprint, request, jsonify
from models import Task
from db import db

tasks = Blueprint("tasks", __name__)

@tasks.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = Task(
        title=data["title"],
        priority=data["priority"]
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "task created"})

@tasks.route("/tasks", methods=["GET"])
def get_tasks():
    priority = request.args.get("priority")
    completed = request.args.get("completed")
    query = Task.query

    if priority:
        query = query.filter_by(priority=priority)
    if completed:
        query = query.filter_by(completed=completed)

    tasks = query.order_by(Task.created_at.desc()).all()

    result = []
    for t in tasks:
        result.append({
            "id":t.id,
            "title":t.title,
            "priority":t.priority,
            "completed": t.completed,
            "created_at": t.created_at
        })
    return jsonify(result)

@tasks.route("/tasks/<int:id>/toggle", methods=["PUT"])
def toggle_task(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return ({"message": "updated"})

@tasks.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "deleted"})
