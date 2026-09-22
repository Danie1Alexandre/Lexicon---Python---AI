# Part A - Classes and objects.
# 1------------
# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages


# book1 = Book(
#     title = "REd",
#     author= "ben",
#     pages = 200
# )
# book2 = Book(
#     title = "green",
#     author= "anna",
#     pages = 500
# )
# book3 = Book(
#     title = "black",
#     author= "david",
#     pages = 2000
# )
# book4 = Book(
#     title = "blue",
#     author= "jmmy",
#     pages = 450
# )

# print(book1.title, book1.author, book1.pages)
# print(book2.title, book2.author, book2.pages)
# print(book3.title, book3.author, book3.pages)
# print(book4.title, book4.author, book4.pages)

# #2----

# class Laptop:
#     def __init__(self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price

# laptop1 = Laptop(brand="Apple", model="MacBook Air", ram_gb=16, price=15000)
# laptop2 = Laptop(brand="ASUS", model="ZenBook", ram_gb=8, price=10000)
# laptop3 = Laptop(brand="Lenovo", model="ThinkPad", ram_gb=32, price=18000)


# print(laptop1.price)
# laptop1.price = 100
# print(laptop1.price)

#3----

# Part B- mathod and state ---------

#1

# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def is_long(self):
#         if self.pages > 300:
#             return True
#         else:
#             return False

# book1 = Book(
#     title = "REd",
#     author= "ben",
#     pages = 200
# )

# print(book1.is_long())


# part C - Instance and class attributes -----

#1 ----------
# class Product:
#     def __init__(self, name, price):
#         self.name = name  #Instance attribute
#         self.price = price

# product1 = Product("banana", 45)

# print(product1.name)
# print(product1.price)


# 2 ------------------

# class Product:
#     tax_rate =  0.1 #class attribute

#     def __init__(self, name, price):
#         self.name = name  #Instance attribute
#         self.price = price

# 3 -------------------------

class Product:
    tax_rate =  0.1 #class attribute

    def __init__(self, name, price):
        self.name = name  #Instance attribute
        self.price = price
    
    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

product1 = Product("banana", 45)
print(product1.price_with_tax())