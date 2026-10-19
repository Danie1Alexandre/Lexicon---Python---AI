import requests

from api_client import get_json

#1
# response = requests.get("https://fakestoreapi.com/products")
# products = response.json()
# sorted_product = sorted(products, key= lambda product:product["price"])

# for product in sorted_product:
#     print(f"price: {product['price']} name: {product['title']}")


#2
response = get_json("https://fakestoreapi.com/products/categories")
categorys = response

print(categorys)

user_input = input('pick category: ')
response = requests.get(f"https://fakestoreapi.com/products/category/{user_input}")
products = response.json()
print(len(products))
cheapest = min(products, key=lambda product: product['price'])
print(f"{cheapest['title']} Price: {cheapest['price']}")


