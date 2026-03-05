from flask import Flask, request, jsonify
import io
import json
import csv

app = Flask(__name__)

def load_products():
    try:
        with open("products.json", 'r') as f:
            return json.load(f)
    except:
        return []
    
def save_products(products):
    try: 
        with open("products.json", 'w') as f:
            json.dump(products, f, indent=2)
    except Exception as e:
        return e

@app.route("/upload", methods=["POST"])
def upload_csv():
    file = request.files["file"]
    stream = io.StringIO(file.stream.read().decode("utf-8"))
    reader = csv.DictReader(stream)

    products = load_products()

    total_rows = 0
    products_added = 0
    failed_rows = 0

    for row in reader:
        total_rows += 1

        name = row.get("name")
        price = row.get("price")
        stock = row.get("stock")

        price = float(price)
        stock = int(stock)

        if price <= 0 or stock <= 0:
            failed_rows += 1
            continue

        try:
            product = {
                "name": name,
                "price": price,
                "stock": stock
            }

            products.append(product)
            products_added += 1

        except:
            failed_rows += 1

    save_products(products)

    return jsonify({
        "total_rows": total_rows,
        "products_added": products_added,
        "failed_rows": failed_rows
    })

if __name__ == "__main__":
    app.run(debug=True)