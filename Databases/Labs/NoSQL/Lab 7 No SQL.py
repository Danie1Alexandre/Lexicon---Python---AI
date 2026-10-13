from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)

db = client["webshop"]

products = db["products"]


query = {"category": "Accessories"}

results = products.find(query,{"_id": 0, "name": 1})

for product in results:
    print(product["name"])