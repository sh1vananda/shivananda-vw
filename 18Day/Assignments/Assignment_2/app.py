from flask import Flask

from auth import auth
from products import products

app = Flask(__name__)
app.secret_key = "secret"

app.register_blueprint(auth)
app.register_blueprint(products)

if __name__ == "__main__":
    app.run(debug=True)