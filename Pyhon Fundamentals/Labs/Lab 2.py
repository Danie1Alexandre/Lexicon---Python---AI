#1 List
# Languages = ["java", "python", "c++", "c#", "C", "JavaScript", "Ruby", "swift" ]
# print(Languages[0])
# print(Languages[-1])
# print(Languages[-2])

# #2
# print(Languages[:2])
# print(Languages[3:7])
# print(Languages[4:])
# print(Languages[::-1])

# #3
# Languages.append("joker")
# print(Languages)

# Languages.remove("joker")
# print(Languages)

# Languages.insert(1,"joker")
# print(Languages)

# Languages.pop(1)
# print(Languages)

# #4
# numbers = [1, 2, 4, 3, 5, 6, 7, 8,17]   
# print(numbers)                     
# print(len(numbers))  
# print(min(numbers))  
# print(max(numbers))  
# print(sum(numbers))            

# #5
# numbers.sort() #Ascending
# print(numbers)

# numbers.sort(reverse=True) #Decending
# print(numbers)

# new_numbers = sorted(numbers)
# print(new_numbers)
# # sorted creats a new list while sort uses the original list.

# #6
# A = [1, 2, 3]
# B = []

# B = A
# B.append(4)
# print("A:", A)
# print("B:", B)

# #make a copy
# B = A.copy()
# B.append(5)
# print("A:", A)
# print("B:", B)

# 2 tupleas and unpacking

# #1
# rgb = ("red", "green", "blue")
# r,g,b= rgb
# print(r,g,b)
# print(g)
# print(b)

# #2
# person = ("Ada", 30, "stockholm")
# name, age, city = person
# print(f"  {name}, is {age} and lives in {city}")


#3
# tuple_numbers =(1, 2, 3)

# try:
#     tuple_numbers[1] = 7 #this is not allowed on tuples
# except TypeError as e:
#     print(f"error: {e}")

# # Tuples are useful when you have data 
# # that should not be changed afterwards. 
# # Prevents accidental changes.
    
# #4
# coordinates = [
#     (10, 20),
#     (14, 27),
#     (50, 30),
#     (40, 25)
# ] 

# coordinates_x1 = coordinates[0][0]
# coordinates_y1 = coordinates[0][1]

# coordinates_x4 = coordinates[3][0]
# coordinates_y4 = coordinates[3][1]

# print("coordinates 1: ", coordinates_x1, coordinates_y1)
# print("coordinates 4: ", coordinates_x4, coordinates_y4)

# Sets

# #1
# course = ["python", "python", "java", "sfi", "java"]
# set_course = set(course)

# print(course)
# print(set_course)

# #compare lenght
# print("before", len(course))
# print("after", len(set_course))

# #2
# skils1= {"python","java","html", "css"}
# skils2= {"python","java","C#", "Ruby"}

# shared_skils = skils1 & skils2 #Intersection
# print("shared_skils: ", shared_skils)

# person_1_skill = skils1 -skils2 #difference
# print("person_1_skill: ", person_1_skill)

# skill_union = skils1|skils2 #Union
# print("all skills: ",skill_union)

# #3 
# Names = {"bob", "anna", "david"}
# print(Names)

# Names.add("benny")
# print(Names)

# Names.remove("benny")
# print(Names)

# Names.discard("carl")#discard dont give error like remove

# Names.add("carl")
# print(Names)

# Names.remove("carl")
# print(Names)

# print("bob" in Names) #mebership
# is_member = "anna" in Names
# print(is_member)
# print("bob" not in Names) 
# print("Lisa" in Names)


#4
# Unlike lists, sets only use unique values . 
# sets can be used for unique usernames on a webshop
# sets can see if a name are available or not. 


# part D - Dictionaries

# 1#  
# Laptop ={
#     "brand": "intel",
#     "model": "ai 1",
#     "RAM"  : 8,
#     "storage_gb": 200,
#     "price": 2000
# }

# print(Laptop["brand"])
# print(Laptop["model"])
# print(Laptop["RAM"])
# print(Laptop["storage_gb"])
# print(Laptop["price"])

# # 2

# Laptop["price"] = 2500
# print(f"new price {Laptop['price']}")
# Laptop["OS"] = "windows"
# del Laptop["RAM"]

# #3

# print (Laptop.get("model"))
# print (Laptop.get("cpu")) #cpu is not a key, so we get None instead

# # #4 
# print("keys", list(Laptop.keys()))
# print("values", list(Laptop.values()))
# print("items", list(Laptop.items()))

# for key, value in Laptop.items():
#     print(f"{key.capitalize()}: {value}")


#5

# study_hours = {
#     "Math": 15,
#     "Python": 25,
#     "English": 10,
#     "Physics": 20,
#     "History": 8
# }

# total_hours_loop = 0
# for hours in study_hours.values():
#     total_hours_loop += hours

# print("Total:", total_hours_loop)

# Part E - Nested Collections 

# books = [
#     {
#         "title": "book1",
#         "author": "author1",
#         "pages": 500,
#         "available": True
#     },
#     {
#         "title": "book2",
#         "author": "author2",
#         "pages": 500,
#         "available": True
#     },
#     {
#         "title": "book3",
#         "author": "author3",
#         "pages": 500,
#         "available": True
#     },
#     {
#         "title": "book4",
#         "author": "author4",
#         "pages": 500,
#         "available": True
#     },
#     {
#         "title": "book5",
#         "author": "author5",
#         "pages": 500,
#         "available": False
#     }
# ]
# #2
# print(books[2]["title"])
# print(books[-1]["available"])

# #3
# print(books[0]["title"])
# books[0]["title"] = "robinhood"
# print(books[0]["title"])

# books[3]["color"] = "red"
# print(books[3])

# #4

# department_dictionary = {
#     "department1": ["robin", "joker"],
#     "department2": ["max", "anna"],
#     "department3": ["even", "steven"]
# }

# print(department_dictionary["department1"])
# print(department_dictionary["department1"][1])

# #5

# courses = [
#     {
#         "name": "Python",
#         "teacher": "bob",
#         "topics": ["str", "class", "loops"]
#     },

#     {
#         "name": "english",
#         "teacher": "sven",
#         "topics": ["words", "spelling", "talk"]
#     },

#     {
#         "name": "math",
#         "teacher": "anna",
#         "topics": ["adition", "subtractcion", "division"]
#     }
# ]

# print(courses[1]["teacher"])
# print(courses[2]["topics"][2])

# Part F - Applied challenge: Personal meida catalogue

