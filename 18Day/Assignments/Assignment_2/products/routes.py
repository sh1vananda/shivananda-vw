from flask import render_template, request, session, redirect, url_for, make_response
import json
from . import products

def load_products():
    with open("products.json", 'r') as f:
        products = json.load(f)
    
    for i, p in enumerate(products):
        p["id"] = i

    return products

    
def update_recent(response, product_id):
    cookie = request.cookies.get("recent_products")

    if cookie:
        ids = cookie.split(", ")
    else:
        ids = []

    if str(product_id) in ids:
        ids.remove(str(product_id))

    ids.append(str(product_id))

    if len(ids) > 5:
        ids = ids[-5:]
    
    response.set_cookie("recent_products", ",".join(ids))

    return response

@products.route("/")
def get_products():
    if "username" not in session:
        return redirect(url_for("auth.login"))
    
    products = load_products()

    return render_template("products.html", products=products)

@products.route("/product/<int:pid>")
def view_product(pid):
    if "username" not in session:
        return redirect(url_for("auth.login"))
    
    products = load_products()

    product = next((p for p in products if p["id"] == pid), None)

    if not product:
        return "Product not found"
    
    response = make_response(render_template("product.html", product=product))
    response = update_recent(response, pid)

    return response

@products.route("/recent")
def recent_products():
    if "username" not in session:
        return redirect(url_for("auth.login"))
    
    cookie = request.cookies.get("recent_products")

    if not cookie:
        return render_template("recent.html", products=[])
    
    ids = cookie.split(",")

    products = load_products()

    recent = [p for p in products if str(p["id"]) in ids]

    return render_template("recent.html", products=recent)