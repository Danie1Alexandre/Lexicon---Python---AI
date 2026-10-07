SELECT COUNT(*) FROM orders;
 
INSERT INTO customers(customer_id, first_name, last_name, email, city, joined_date)
VALUES (11,'daniel', 'alex', 'x@example.com', 'stockholm', '2026-10-07');


SELECT * from products;
INSERT INTO products(name, category, price, stock)
VALUES
	('Scarf', 'Accessories', 229, 15),
	('Gloves', 'Accessories', 199, 20);
SELECT * from orders;	
INSERT INTO orders (customer_id, order_date, status)
VALUES (7, '2026-10-07', 'new')	
--DELETE FROM orders
--where customer_id = 7;
SELECT * from order_items;	
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 2, 179);



			