from flask import Blueprint, request, render_template, redirect, url_for
from db import db
from models.order import Order
from sqlalchemy import func, select
 
orders_bp = Blueprint("orders", __name__)
 
@orders_bp.route("/")
def home():
    orders = Order.query.all()
    return render_template("orders.html", orders=orders)
 
@orders_bp.route("/orders", methods=["POST"])
def add_order():
    product = request.form.get("product_name")
    quantity = int(request.form.get("quantity"))
    price = int(request.form.get("price"))
    order = Order(product_name=product, quantity=quantity, price=price)
    db.session.add(order)
    db.session.commit()
    return redirect(url_for("orders.home"))
 
@orders_bp.route("/orders/revenue")
def revenue_per_day():
    revenue = db.session.query(
        func.sum(Order.price * Order.quantity)
    ).scalar() 
    return f"Total Revenue: {revenue}"

@orders_bp.route("/orders/high")
def high_revenue_orders():
    orders = db.session.query(Order).filter(Order.price * Order.quantity > 2000).all()
    result = []
    for o in orders:
        revenue = o.price*o.quantity
        result.append(f"{o.product_name} : {revenue}")
    return "<br>".join(result)