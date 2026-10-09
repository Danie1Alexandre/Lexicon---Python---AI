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
WHERE city = 'Uppsala' or city = 'Stockholm'
