import sqlite3

conn = sqlite3.connect("webshop.db")

cursor = conn.cursor()

cursor.execute("select first_name, last_name, city FROM customers")
customers = cursor.fetchall()


for first, last, city in customers:
    print (f" {first} {last} {city}")