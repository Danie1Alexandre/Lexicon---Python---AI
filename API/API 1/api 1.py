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


# new_product = {
#     "title": "new",
#     "price": 1299.50,
#     "description": "new",
#     "image": "https://",
#     "category": "electronics"
# }


# product  = requests.post("https://fakestoreapi.com/products", json=new_product, timeout= 5)

# print(f"status_code: {product.status_code}")
# print(product.json())

# patch = requests.patch("https://fakestoreapi.com/products/7", json = {"price": 1499.00}, timeout=5)

# print(patch.status_code)
# print(patch.json())

#5

# try :
#     response = requests.get("//fake.com")
# except requests.exceptions.MissingSchema: print("wrong url")

# try :

#     response = requests.get("https://fakeeee.com/products")

# except requests.exceptions.ConnectionError: print("wrong domain")

# try :
#     response = requests.get("https://fakestoreapi.com/products/7", timeout= 0.001)


# except requests.exceptions.ConnectTimeout: print("connection timeout")

#part 2

response = requests.get('https://geocoding-api.open-meteo.com/v1/search', params={"name": "Stockholm", "count": 1})

data= response.json()


lat = data["results"][0]["latitude"]
lon = data["results"][0]["longitude"]

print(f"Latitude: {lat}")
print(f"Longitude: {lon}")

weather_params = {
    "latitude": lat,
    "longitude": lon,
    "current": "temperature_2m,wind_speed_10m"
}

response = requests.get("https://api.open-meteo.com/v1/forecast", params = weather_params)

weather_data = response.json()

current_weather = weather_data["current"]
print(current_weather)
print(f"Temperature: {current_weather['temperature_2m']}°C")
print(f"wind speed 10m: {current_weather['wind_speed_10m']} m/s")
