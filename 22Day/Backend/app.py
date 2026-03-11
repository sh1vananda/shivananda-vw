from flask import Flask
from datetime import datetime
from flask_cors import CORS
from db import db
from routes import tasks

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/test_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

CORS(app)

app.register_blueprint(tasks)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)