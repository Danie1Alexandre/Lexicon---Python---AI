SELECT COUNT(*) FROM orders;

SELECT * FROM products 
WHERE (category = 'Clothing' or category = 'Accessories')
and price BETWEEN 150 and 500
ORDER BY price DESC;

SELECT * from orders
WHERE orders.order_date LIKE '2026-02%'
and NOT status  = 'cancelled'

SELECT order_items.order_id, products.name, order_items.quantity, (order_items.quantity*order_items.unit_price) AS line_total
FROM order_items
JOIN products ON order_items.product_id = products.product_id
WHERE line_total > 500
ORDER BY price DESC;

SELECT DISTINCT customers.first_name, customers.city
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
WHERE city = 'Uppsala' or city = 'Stockholm';

INSERT INTO customers (first_name, last_name, city)
VALUES ('Leo', 'Falk', 'Uppsala');
INSERT INTO orders (order_id, customer_id, order_date, status)
VALUES (16, 11, '2026-10-09', 'new');
INSERT INTO order_items(order_id, product_id, quantity, unit_price)
VALUES (16, 1, 1, 599),
		(16, 9, 2, 129);
SELECT products.name
FROM products
JOIN order_items ON order_items.product_id = products.product_id
JOIN orders on orders.order_id = order_items.order_id
WHERE orders.order_id = 16;




