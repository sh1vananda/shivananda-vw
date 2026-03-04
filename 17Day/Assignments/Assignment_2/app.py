from flask import Flask

from products import products
from cart import cart
from orders import orders

app = Flask(__name__)

app.register_blueprint(products)
app.register_blueprint(cart)
app.register_blueprint(orders)

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)