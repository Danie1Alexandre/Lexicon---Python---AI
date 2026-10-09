SELECT COUNT(*) FROM orders;

SELECT * FROM products 
WHERE (category = 'Clothing' or category = 'Accessories')
and price BETWEEN 150 and 500
ORDER BY price DESC;


