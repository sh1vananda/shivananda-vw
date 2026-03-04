from flask import render_template, request, redirect, url_for, make_response
import json
from . import products

PRODUCT_LIST = [
    {"id": 1, "name": "Product 1", "price": 1000},
    {"id": 2, "name": "Product 2", "price": 2000},
    {"id": 3, "name": "Product 3", "price": 3000},
    {"id": 4, "name": "Product 4", "price": 4000},
    {"id": 5, "name": "Product 5", "price": 5000},
]

@products.route("/")
def list_products():
    return render_template("products.html", products=PRODUCT_LIST)


@products.route("/add/<int:pid>")
def add_to_cart(pid):
    cart_cookie = request.cookies.get("cart")

    if cart_cookie:
        cart = json.loads(cart_cookie)
    else:
        cart = {}

    pid = str(pid)

    if pid in cart:
        cart[pid] += 1
    else:
        cart[pid] = 1
    
    response = make_response(redirect(url_for("products.list_products")))
    response.set_cookie("cart", json.dumps(cart))
    
    return response