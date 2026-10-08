SELECT count(*) FROM orders;

SELECT 
customers.first_name, customers.last_name,
orders.status 
FROM orders
JOIN customers ON customers.customer_id = orders.customer_id

SELECT customers.first_name, customers.last_name,
orders.order_id, orders.customer_id,
orders.order_date, orders.status
FROM orders 
JOIN customers ON customers.customer_id = orders.customer_id
WHERE customers.first_name = 'Erik';

SELECT o.order_id, o.customer_id, o.order_date, o.status,
c.first_name, c.last_name,  c.city 
FROM orders o 
JOIN customers c on o.customer_id = c.customer_id
WHERE c.city = 'Göteborg'
ORDER BY o.order_date DESC;

SELECT * FROM order_items

SELECT order_items.order_id, order_items.product_id,
products.name, products.category
FROM order_items
JOIN products ON products.product_id = order_items.product_id;

SELECT order_items.order_id, products.name
FROM order_items
JOIN products ON products.product_id = order_items.product_id
WHERE products.category = 'Shoes';

SELECT products.name,order_items.quantity, order_items.unit_price,
(order_items.quantity * order_items.unit_price) as line_total,
sum (order_items.quantity * order_items.unit_price) OVER() as order_total
FROM order_items
JOIN products on products.product_id = order_items.product_id
JOIN orders on orders.order_id = order_items.order_id
WHERE orders.order_id = 10; 

SELECT customers.first_name, orders.order_date
FROM order_items
JOIN orders ON orders.order_id = order_items.order_id
JOIN customers ON customers.customer_id = orders.customer_id
JOIN products ON products.product_id = order_items.product_id
WHERE products.name = "Hoodie Black"

SELECT customers.first_name, orders.order_id, orders.order_date, orders.status
FROM customers
left JOIN orders ON orders.customer_id = customers.customer_id;

SELECT  products.name
FROM products
LEFT JOIN order_items ON order_items.product_id = products.product_id
WHERE order_items.order_id IS NULL

SELECT customers.first_name, products.name, order_items.quantity
FROM order_items
JOIN orders ON orders.order_id = order_items.order_id
JOIN customers ON customers.customer_id = orders.customer_id
JOIN products ON  products.product_id = order_items.product_id
WHERE customers.city = 'Uppsala' 
ORDER BY customers.first_name

