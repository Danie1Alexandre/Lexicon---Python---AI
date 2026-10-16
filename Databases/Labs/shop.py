import sqlite3


def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")

def change_stock_of_product(conn):
    product_id =  int (input("product id: "))
    new_stock = int (input("new stock: "))
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE products
        SET stock = ?
        WHERE product_id = ?
    """,(new_stock, product_id))
    conn.commit()
    print("stock updated!")

def receipt(conn):
    order_id =  int (input("order id: "))
    cursor = conn.cursor()
    total_order_sum = 0    
    
    cursor = conn.execute("""
        SELECT products.name, order_items.quantity, products.price  
        FROM products
        JOIN order_items ON order_items.product_id = products.product_id
        JOIN orders ON orders.order_id = order_items.order_id
        WHERE orders.order_id = ?          
    """, (order_id,))

    items = cursor.fetchall()
    for name, quantity, price in items:
        item_total = quantity * price
        total_order_sum += item_total
        print(f"{name:<15} {quantity}x {price:>6} kr = {item_total:>7} kr")
        print("-"*30)
        print(f"TOTAL SUM: {total_order_sum:>19} kr")


def best_selling_products(conn):
    
    cursor = conn.cursor()
    cursor.execute("""
        SELECT products.name, SUM(order_items.quantity) AS total_sold
        FROM products
        JOIN order_items On order_items.product_id = products.product_id
        GROUP BY products.product_id   
        ORDER BY total_sold DESC
        LIMIT 3
    """)
    items = cursor.fetchall()
    for index, (name, total_sold) in enumerate(items, start = 1):
        print(f"{index}, {name}, Total Sold: {total_sold}")


def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product 4) Change Stock 5) receipt 6) Best Selling Products  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock_of_product(conn)
        elif choice == "5":
            receipt(conn)
        elif choice == "6":
            best_selling_products(conn)
        elif choice == "0":
            break
    conn.close()

main()
