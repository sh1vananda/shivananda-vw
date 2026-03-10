from flask import Flask
from db import db
from routes.books import books_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/test_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(books_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)