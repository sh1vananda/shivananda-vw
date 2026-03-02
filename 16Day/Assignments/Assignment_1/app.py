from flask import Flask, render_template, request

app = Flask(__name__)

product_data = [
    {"id": 1, "name": "product 1", "price": 1000, "category": "electronics", "available": True},
    {"id": 2, "name": "product 2", "price": 2000, "category": "apparel", "available": True},
    {"id": 3, "name": "product 3", "price": 3000, "category": "electronics", "available": False},
    {"id": 4, "name": "product 4", "price": 4000, "category": "electronics", "available": True},
    {"id": 5, "name": "product 5", "price": 5000, "category": "apparel", "available": False},
    {"id": 6, "name": "product 6", "price": 6000, "category": "electronics", "available": True},
    {"id": 7, "name": "product 7", "price": 7000, "category": "books", "available": True},
    {"id": 8, "name": "product 8", "price": 8000, "category": "books", "available": True},
    {"id": 9, "name": "product 9", "price": 9000, "category": "books", "available": True},
    {"id": 10, "name": "product 10", "price": 10000, "category": "apparel", "available": True}
]

@app.route("/products")
def products():
    products = product_data.copy()
    category = request.args.get("category")

    if category:
        products = [product for product in products if product["category"] == category]
    
    available = request.args.get("available")
    if available:
        if available.lower() == "true":
            products = [product for product in products if product["available"]]
        elif available.lower() == "false":
            products = [product for product in products if not product["available"]]
    
    sort = request.args.get("sort")
    if sort == "asc":
        products = sorted(products, key=lambda x: x["price"])
    elif sort == "desc":
        products = sorted(products, key=lambda x: x["price"], reverse=True)

    total = len(products)

    return render_template("products.html", products=products, total=total)

if __name__ == "__main__":
    app.run(debug=True)