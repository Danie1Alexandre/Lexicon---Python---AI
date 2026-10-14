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