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

for product in db.products.find().sort("price", 1):
    print(f"{product['name']:<25} {product['price'] :<8}")