SELECT * FROM customers;
SELECT name, category FROM products WHERE category = "Shoes";
SELECT first_name, last_name, city FROM customers where city = 'Uppsala';
SELECT name, price FROM products WHERE price = 199;
SELECT * FROM products ORDER BY name ASC;
SELECT * FROM customers ORDER BY joined_date;
SELECT * FROM products WHERE stock = 0;
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;
SELECT first_name, city FROM customers WHERE city = 'Stockholm' OR city = 'Göteborg';
SELECT name AS products, price AS price_sek FROM products;
SELECT * FROM products WHERE (category = 'Clothing' OR category = 'Shoes') AND price > 1000;
SELECT name, price, stock, price*stock AS stock_value FROM products WHERE stock > 1;
SELECT first_name FROM customers WHERE first_name like '____';
SELECT price FROM products 
ORDER BY price ASC
LIMIT 5 OFFSET 5;
SELECT * FROM customers WHERE joined_date < 2025 AND NOT city = 'Uppsala' 
