import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

#1
# cursor.execute("select first_name, last_name, city FROM customers")
# customers = cursor.fetchall()
# for first, last, city in customers:
#     print (f" {first} {last} {city}")

#2
max_price = 300

cursor.execute("select price FROM products WHERE price <= ?",(max_price,))
prices = cursor.fetchall()

for price in prices:
    print (f" {price[0]}")

cursor.close()
conn.close()