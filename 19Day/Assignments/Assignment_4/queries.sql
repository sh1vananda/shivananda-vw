SELECT customer_id, SUM(total_amount) AS total_spent
FROM eorders
GROUP BY customer_id;

SELECT customer_id, COUNT(order_id) AS order_count
FROM eorders
GROUP BY customer_id;

SELECT customer_id
FROM eorders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

SELECT customer_id
FROM eorders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000;

SELECT product_id
FROM eorders
GROUP BY product_id
HAVING SUM(quantity) > 100;