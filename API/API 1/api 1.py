from api_client import get_json #3
import requests

#1
# response = requests.get("https://fakestoreapi.com/products")
# products = response.json()
# sorted_product = sorted(products, key= lambda product:product["price"])

# for product in sorted_product:
#     print(f"price: {product['price']} name: {product['title']}")


#2
# categorys = get_json("https://fakestoreapi.com/products/categories")

# print(categorys)

# user_input = input('pick category: ')
# products = get_json(f"https://fakestoreapi.com/products/category/{user_input}")

# print(len(products))
# cheapest = min(products, key=lambda product: product['price'])
# print(f"{cheapest['title']} Price: {cheapest['price']}")

#4


new_product = {
    "title": "new",
    "price": 1299.50,
    "description": "new",
    "image": "https://pravatar.cc",
    "category": "electronics"
}


new_product = response = requests.post("https://fakestoreapi.com/products", json=new_product, timeout= 5)

print(f"status_code: {new_product.status_code}")
print(new_product.json())
