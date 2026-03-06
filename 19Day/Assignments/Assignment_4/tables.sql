CREATE TABLE eorders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10,2)
);