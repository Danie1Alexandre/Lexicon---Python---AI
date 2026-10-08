SELECT count(*) FROM orders;

SELECT 
customers.first_name, customers.last_name,
orders.status 
FROM orders
JOIN customers ON customers.customer_id = orders.customer_id

