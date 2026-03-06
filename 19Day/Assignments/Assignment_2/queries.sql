SELECT customer_id
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

SELECT c.customer_name, SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 5;

SELECT product_id
FROM order_items
GROUP BY product_id
ORDER BY SUM(quantity) DESC
LIMIT 1;

SELECT *
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id FROM orders
);

SELECT MONTH(order_date) AS month, SUM(total_amount) AS revenue
FROM orders
GROUP BY MONTH(order_date);