SELECT * FROM customers;
SELECT name, category FROM products WHERE category = "Shoes";
SELECT first_name, last_name, city FROM customers where city = 'Uppsala';
SELECT name, price FROM products WHERE price = 199;
SELECT * FROM products ORDER BY name ASC;
SELECT * FROM customers ORDER BY joined_date;
SELECT * FROM products WHERE stock = 0;
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;