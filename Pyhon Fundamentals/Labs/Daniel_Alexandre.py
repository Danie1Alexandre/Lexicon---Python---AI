# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4}, 
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3}, 
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}  
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
def seperater():
    print("-"*40)
print("All products")
for product in products:
    print("product:", product["name"], "price:", product["price"], "stock:", product["stock"])

seperater()
print("In Stock")
for product in products:
    if product["stock"] > 0:
        print("product:", product["name"], "price:", product["price"], "stock:", product["stock"])
seperater()
print("Total value of Stock")
total_value_stock= 0
for product in products:
        pxp =  product["price"] * product["stock"]

        total_value_stock +=pxp

print(total_value_stock)
seperater()
print("most expensiv product")
most_expensive = 0
for product in products:
     if product["price"] > most_expensive:
          most_expensive = product["price"]
          most_expensive_name = product["name"]
print(most_expensive_name)
seperater()
     

# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:

def calculate_average(scores):
    total_score =0
     
    for score in scores:
        total_score += score
    
    return total_score/ len(scores)

def create_result(scores):
    average = calculate_average(scores)
    if average >= 70:
         return "pass"
    else:
        return  "fail"

result = create_result(scores)

print ("average ", calculate_average(scores),"result", result)

seperater()

# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

product_prices = [100, 500, 200]
order_settings = {"discount": 0.10, "shipping": 20}

def calculate_order(customer,*prices,**settings):
    sub_total= sum(prices)

    final_total = sub_total

    if "discount" in settings:
         final_total -= (final_total * settings["discount"])
    
    if "shipping" in settings:
        final_total += settings["shipping"]

    return {
        "customer": customer,
        "subtotal": sub_total,
        "final_total": final_total,
        "settings": settings
    }

total = calculate_order("Anna", *product_prices, **order_settings)

print(total) 

seperater()


# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
normalized_player_names = [player["name"].strip().capitalize()for player in players]
print(normalized_player_names)
seperater()

player_score = [player for player in players if player["active"] and player["score"] >= 80]
print(player_score)
seperater()

sorted_player_score = sorted(players, key=lambda player:player["score"], reverse= True)
print(sorted_player_score)
seperater()

for index, player in enumerate(sorted_player_score, start=1):
    new_n = player["name"].strip().capitalize()
    print(index, new_n, player["score"] )

seperater()

player_name = [player["name"] for player in players]
print(player_name)

player_score_list = [player["score"] for player in players]
print(player_score_list)

for name, score in zip(player_name,player_score_list):
     print(f"name {name} score {score}" )

