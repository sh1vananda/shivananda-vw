from flask import Flask
from db import db
from routes.auth import auth_bp
from routes.employees import emp_bp
 
app = Flask(__name__)
app.secret_key = "secret"
 
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/test_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
db.init_app(app)
 
app.register_blueprint(auth_bp)
app.register_blueprint(emp_bp)
 
with app.app_context():
    db.create_all()
 
if __name__ == "__main__":
    app.run(debug=True)
 
 
 
