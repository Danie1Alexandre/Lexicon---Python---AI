SELECT COUNT(*) FROM orders;

SELECT * FROM products 
WHERE (category = 'Clothing' or category = 'Accessories')
and price BETWEEN 150 and 500
ORDER BY price DESC;

SELECT * from orders
WHERE orders.order_date LIKE '2026-02%'
and NOT status  = 'cancelled'
