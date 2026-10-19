import requests

response = requests.get("https://fakestoreapi.com/products")
products = response.json()
sorted_product = sorted(products, key= lambda product:product["price"])

for product in sorted_product:
    print(f"price: {product['price']} name: {product['title']}")


