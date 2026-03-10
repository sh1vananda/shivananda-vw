from flask import Blueprint, render_template, request, redirect, session
from db import db
from decorators import role_required
from models.employee import Employee
 
emp_bp = Blueprint("employees", __name__)
 
@emp_bp.route("/employees")
@role_required(["admin","manager"])
def employees():
    employees = Employee.query.all()
    print(session)
    return render_template("employees.html", employees=employees)
 
@emp_bp.route("/employee/<int:id>")
def view_employee(id):
    emp = Employee.query.get(id)
    return render_template("employee_profile.html", emp=emp)
 
@emp_bp.route("/employee/<int:id>/edit", methods=["GET","POST"])
def edit_employee(id):
    emp = Employee.query.get(id)
    role = session.get("role")
    user_id = session.get("user_id")
    allowed = False
    if role == "admin":
        allowed = True
    if role == "manager" and emp.manager_id == user_id:
        allowed = True
    if role == "employee" and emp.id == user_id:
        allowed = True
    if not allowed:
        return "Access Denied"
    if request.method == "POST":
        emp.name = request.form.get("name")
        emp.email = request.form.get("email")
        emp.department = request.form.get("department")
        db.session.commit()
        return redirect(f"/employee/{id}")
    return render_template("employee_profile.html", emp=emp)
 
@emp_bp.route("/employee/<int:id>/delete")
@role_required(["admin"])
def delete_employee(id):
    emp = Employee.query.get(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect("/employees")