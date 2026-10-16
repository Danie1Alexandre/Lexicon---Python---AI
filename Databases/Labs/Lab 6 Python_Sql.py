import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

#1
# cursor.execute("select first_name, last_name, city FROM customers")
# customers = cursor.fetchall()
# for first, last, city in customers:
#     print (f" {first} {last} {city}")

#2
# max_price = 300

# cursor.execute("select price FROM products WHERE price <= ?",(max_price,))
# prices = cursor.fetchall()

# for price in prices:
#     print (f" {price[0]}")


#3
# category = "Clothing"

# cursor.execute("SELECT count() name  FROM products WHERE category = ?", (category,))
# clothing = cursor.fetchall()

# for cloth in clothing:
#     print (f" {cloth[0]}")

#4
# You nedd to tell SQL that you are sending a text string and not code?
# A placeholder seprte the user input from the sql question.

#5
# def change_stock_of_product(conn):
#     product_id =  int (input("product id: "))
#     new_stock = int (input("new stock: "))
#     cursor = conn.cursor()
#     cursor.execute("""
#         UPDATE products
#         SET stock = ?
#         WHERE product_id = ?
#     """,(new_stock, product_id))
#     conn.commit()
#     print("stock updated!")

#6
# def receipt(conn):
#     order_id =  int (input("order id: "))
#     cursor = conn.cursor()
#     total_order_sum = 0    
    
#     cursor = conn.execute("""
#         SELECT products.name, order_items.quantity, products.price  
#         FROM products
#         JOIN order_items ON order_items.product_id = products.product_id
#         JOIN orders ON orders.order_id = order_items.order_id
#         WHERE orders.order_id = ?          
#     """, (order_id,))

#     items = cursor.fetchall()
#     for name, quantity, price in items:
#         item_total = quantity * price
#         total_order_sum += item_total
#         print(f"{name:<15} {quantity}x {price:>6} kr = {item_total:>7} kr")
#         print("-"*30)
#         print(f"TOTAL SUM: {total_order_sum:>19} kr")



#7
#ValueError: could not convert string to float: 'asc'
# you cant add strin casue datbes ask for int a (numbers)

#8
# def best_selling_products(conn): 
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT products.name, SUM(order_items.quantity) AS total_sold
#         FROM products
#         JOIN order_items On order_items.product_id = products.product_id
#         GROUP BY products.product_id   
#         ORDER BY total_sold DESC
#         LIMIT 3
#     """)
#     items = cursor.fetchall()
#     for index, (name, total_sold) in enumerate(items, start = 1):
#         print(f"{index}, {name}, Total Sold: {total_sold}")

#9
# cursor.execute("""
# SELECT DISTINCT products.name
# FROM order_items
# JOIN products ON products.product_id = order_items.product_id
# JOIN orders ON orders.order_id = order_items.order_id
# JOIN customers ON customers.customer_id = orders.customer_id
# WHERE customers.customer_id = 1
#  """)              
# anna_product_info = cursor.fetchall()

# for product in anna_product_info:
#     print(product[0])

#10

# cursor.execute("""
#     UPDATE customers
#     SET email = ?
#     WHERE first_name = 'Erik'
                 
# """,["erik.johansson@example.com"])
# conn.commit()


#11

# cursor.execute("""
# SELECT customers.customer_id, customers.first_name , customers.city, count(orders.order_id)
# FROM customers
# LEFT JOIN orders ON orders.customer_id = customers.customer_id
# GROUP BY customers.customer_id, customers.first_name , customers.city               
# """)
# customer_overview = cursor.fetchall()
# for id, first_name, city, order_amount in customer_overview:
#     print(id, first_name, city, order_amount)

#12
# You should only collect information that is needed for the app. 
# # Therefore, "just in case" is not a valid reason ; it creates unnecessary security risk.

cursor.close()
conn.close()