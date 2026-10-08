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

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 0, 179);
-- Result: CHECK constraint failed: quantity > 0 (can not be zero)

SELECT * from orders WHERE order_id = 12;	
UPDATE orders
SET status = 'shipped'
WHERE order_id = 12;

SELECT * from products WHERE name = 'Water Bottle';	
UPDATE products
SET stock = 50
WHERE product_id = 5;

SELECT * from products WHERE category = 'Accessories';
UPDATE products
SET price = price * 1.1
WHERE category = 'Accessories';

SELECT * from orders WHERE status = 'cancelled';
DELETE FROM orders
WHERE status = 'cancelled'
-- Result: FOREIGN KEY constraint failed
-- item is still used in a FOREIGN key, can not be delteted.

SELECT count (*) from orders;

-- student | phone_numbers | course1 | course2 | course3. 
-- A student can have many numbers , not just one. 
-- No key for student or course? 
-- Hard to search on individual courses since they are all in one place. 
-- A student may only read one course ; waste of space to ALWAYS force 3.
 -- Or a student may read 5 courses, but there are only 3 courses in the column.

CREATE TABLE order_sheet 
(  order_no INTEGER,  
	customer TEXT,  
	email    TEXT,  
	city     TEXT,  
	products TEXT,  
	total    REAL
	);

-- breaks 1NF since products have no ID . 
-- Products should not be a list of products, they need a separate table like order_items. 
-- Breaks 2NF since city and email should be in customers. 
-- An order doesn't have an email; a person does.

-- order_id | customer_id | customer_email | order_date. 
-- customer_email doesn't belong here since the table is an ORDER. 
-- email should be in the customer TABLE.

-- "main objects": students - lessons - teachers - instruments 
-- a lesson can be described with this: date -  time - room

-- teachers n---m instruments 
-- teachers 1---n lessons 
-- students n---m lessons 
-- instruments 1---n lessons 
-- some kind of lesson TABLE would tie them all together as the "bridge" (Junction table)
 

			