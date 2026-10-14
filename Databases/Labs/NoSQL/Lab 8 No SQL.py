from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for product in db.products.find({"price": {"$gt": 1000}}):
        print(product["name"], product["price"])