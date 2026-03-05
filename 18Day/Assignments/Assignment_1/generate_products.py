import csv
import random

products = [
    "Laptop","Phone","Keyboard","Mouse","Monitor","Charger","Projector","Headphones","Jeans","Tee"
]

with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "price", "stock"])

    for _ in range(25):
        name = random.choice(products)
        price = round(random.uniform(-10, 2000), 2)
        stock = random.randint(-10, 50)

        writer.writerow([name, price, stock])