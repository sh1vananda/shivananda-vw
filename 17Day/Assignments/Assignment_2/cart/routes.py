from flask import render_template, request, redirect, url_for, make_response
import json
from products.routes import PRODUCT_LIST
from . import cart

def get_cart():
    cart_cookie = request.cookies.get("cart")
    if not cart_cookie:
        return {}
    return json.loads(cart_cookie)

@cart.route("/")
def view_cart():
    cart_data = get_cart()

    items = []
    total = 0

    for p in PRODUCT_LIST:
        pid = str(p["id"])
        if pid in cart_data:
            qty = cart_data[pid]
            subtotal = qty * p["price"]
            items.append({
                "id": pid,
                "name": p["name"],
                "price": p["price"],
                "qty": qty,
                "subtotal": subtotal
            })

            total += subtotal

    return render_template("cart.html", items=items, total=total)

@cart.route("/inc/<pid>")
def inc(pid):
    cart_data = get_cart()
    cart_data[pid] = cart_data.get(pid, 0) + 1

    response = make_response(redirect(url_for("cart.view_cart")))
    response.set_cookie("cart", json.dumps(cart_data))
    return response

@cart.route("/dec/<pid>")
def dec(pid):
    cart_data = get_cart()

    if pid in cart_data:
        cart_data[pid] -= 1
        if cart_data[pid] <= 0:
            del cart_data[pid]

    response = make_response(redirect(url_for("cart.view_cart")))
    response.set_cookie("cart", json.dumps(cart_data))
    return response

@cart.route("/clear")
def clear():
    response = make_response(redirect(url_for("cart.view_cart")))
    response.delete_cookie("cart")
    return response