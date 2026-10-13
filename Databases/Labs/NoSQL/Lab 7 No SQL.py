from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)

db = client["webshop"]

#1
#products_db = db["products"]
# query = {"category": "Accessories"}
# accessories = products_db.find(query,{"_id": 0, "name": 1})
# for product in accessories:
#     print(product["name"])

#2
# for customer in db.customers.find():
#     if customer.get("city", "X") == "Göteborg":
#         print(customer["first_name"], customer["last_name"], customer["city"])

#3
# for product in db.products.find():
#     print(f"{product['name']:<25} {product['price'] :<8}")

#4
# print(db.customers.count_documents({"city": "Uppsala"}))

#5
# print(db.products.find_one({"name": "Sandals"}, {"_id": 0, "stock": 1}))#removes id from the search and prints stock

#6
# for customer in db.customers.find({"newsletter": True}):
#     print(customer["first_name"])

#7

add_me = db.customers.insert_one({
    "fist_name": "dan",
    "last_name" : "alex",
    "email": "exeample@mail.com",
    "city": "Stockholm"   
})

print(add_me.inserted_id)