from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

#1

# for product in db.products.find({"price": {"$gt": 1000}}):
#         print(product["name"], product["price"])

#2

# for order in db.orders.find({"status": {"$ne": "delivered"}}):
#         print(order["_id"], order["status"])

#3

# for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
#     print(customer["first_name"], customer["city"])

#4 

# for product in db.products.find({"details.color": "white"} ):
#          print(product["name"], product["details"]["color"])

# 5
# for product in db.products.find({"tags": "sport"}, {"_id": 0}):
#          print(product["name"], product["tags"])

#6

# for product in db.products.find().sort("price", 1):
#     print(f"{product['name']:<25} {product['price'] :<8}")

#7

# for order in db.orders.find({"items.product_id": 2}):
#     print(f"customer id: {order.get('customer_id')} order id: {order['_id']}")


#8

##check
# for product in db.products.find({"category": "Accessories"}):
#     print(f"{product['name']:<25} {product['price'] :<8}")

##update
# result = db.products.update_many(
#     {"category": "Accessories"},
#     {"$inc": {"price": 20} }
#     )

# print(f"matched {result.matched_count} modified {result.modified_count}")

#9

# result = db.products.find_one(
#     {"name": "Rain Jacket"},

# )
# print(result)

# from datetime import datetime

# result = db.products.update_one(
#     {"name": "Rain Jacket"},
#     {
#         "$addToSet": {"tags": "new"},
#         "$set": {"restock_date": datetime.now()} 
#     }
# )

# print(f"matched {result.matched_count} modified {result.modified_count}")

#10
# from datetime import datetime

# filter = {
#     "status": "new",
#     "order_date": {"$lt": datetime(2026, 3, 20)}
#     }   

# print(db.orders.count_documents(filter))                      

# result = db.orders.delete_many(filter)
# print(f"delted: {result.deleted_count}")