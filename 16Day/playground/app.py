from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", name="ABC")

@app.route('/add/<int:num1>/<int:num2>')
def add_nums(num1, num2):
    return render_template("add.html", sum = num1 + num2)

names = ["abc xyz", "def uvw", "ghi rst", "jkl opq"]

@app.route('/names')
def print_names():
    return render_template("names.html", names=names)

students = [
    {"name": "abc", "marks": 80},
    {"name": "def", "marks": 70},
    {"name": "ghi", "marks": 60},
    {"name": "jkl", "marks": 50},
    {"name": "mno", "marks": 40},
]

@app.route("/grades")
def print_grades():
    return render_template("grades.html", students=students)

@app.route("/search")
def search():
    if "q" in request.args:
        q = request.args.get("q", 1, type=int)
        return f"query parameter = {q}"
    else:
        return "no query parameter passed"
    
@app.route("/google")
def google():
    return redirect("https://www.google.com")

@app.errorhandler(404)
def page_not_found(e):
    return f"<p>{e}</p>", 404

if __name__ == '__main__':
    app.run(debug=True)