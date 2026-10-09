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
