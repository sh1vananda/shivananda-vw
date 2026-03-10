from flask import Blueprint, render_template, request, redirect, session
from models.user import User
 
auth_bp = Blueprint("auth", __name__)
 
@auth_bp.route("/login", methods=["GET","POST"])
def login():
 
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
 
        user = User.query.filter_by(username=username,password=password).first()
 
        if user:
            session["user_id"] = user.id
            session["role"] = user.role
            return redirect("/employees")
 
        return "Invalid credentials"
 
    return render_template("login.html")