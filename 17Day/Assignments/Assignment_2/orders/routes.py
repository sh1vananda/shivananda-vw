from . import orders

@orders.route("/")
def orders_home():
    return "Orders page (placeholder)"