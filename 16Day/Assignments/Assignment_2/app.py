from flask import Flask, render_template, request

app = Flask(__name__)

employees = [
    {"name": "ABC", "department": "HR", "salary": 80000},
    {"name": "ABC", "department": "SAP", "salary": 70000},
    {"name": "ABC", "department": "AI", "salary": 75000},
]

@app.route("/dashboard")
def dashboard():
    role = request.args.get("role").lower()

    if role not in ["admin", "manager", "employee"]:
        return "<p>invalid user role<p>"

    return render_template("dashboard.html", role=role, employees=employees)

if __name__ == "__main__":
    app.run(debug=True)