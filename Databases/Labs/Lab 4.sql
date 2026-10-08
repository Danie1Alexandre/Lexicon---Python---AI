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
WHERE c.city = 'Göteborg';
