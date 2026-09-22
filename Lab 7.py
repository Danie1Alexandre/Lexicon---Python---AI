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

# class Product:
#     tax_rate =  0.1 #class attribute

#     def __init__(self, name, price):
#         self.name = name  #Instance attribute
#         self.price = price
    
#     def price_with_tax(self):
#         return self.price * (1 + self.tax_rate)

# product1 = Product("banana", 45)
# print(product1.price_with_tax())


# Part D - Collections of objects

# 1

# class Student:
#     def __init__(self, name, score):
#         self.name = name    
#         self.score = score

# student1 = Student(name="Alice", score=81)
# student2 = Student(name="Mikael", score=85)
# student3 = Student(name="Ben", score=78)
# student4 = Student(name="Anna", score=90)
# student5 = Student(name="David", score=64)
# student6 = Student(name="Charlie", score=88)

# print(f"{student1.name}: {student1.score} poäng")
# print(f"{student2.name}: {student2.score} poäng")
# print(f"{student3.name}: {student3.score} poäng")
# print(f"{student4.name}: {student4.score} poäng")
# print(f"{student5.name}: {student5.score} poäng")
# print(f"{student6.name}: {student6.score} poäng")

#2 

# students = [ student1, student2, student3, student4, student5, student6]

#3 
# for student in students:
#     print ("student:", student.name, student.score)


# 4 -------

# class Student:
#     def __init__(self, name, score):
#         self.name = name    
#         self.score = score

#     def get_status(self):
#         if self.score >= 70:
#             return "pass"
#         else:
#             return "Fail"


# student1 = Student(name="Alice", score=61)
# student2 = Student(name="Mikael", score=85)
# student3 = Student(name="Ben", score=78)
# student4 = Student(name="Anna", score=90)
# student5 = Student(name="David", score=64)
# student6 = Student(name="Charlie", score=88)

# students = [ student1, student2, student3, student4, student5, student6]

# #5--------
# for student in students:
#     print ("student:", student.name, student.get_status())

# # D6 -------

# passed_students = [student for student in students if student.get_status() == "pass"]
# for student in passed_students:
#     print ("student pass:", student.name, student.get_status())

#Part E - Objects inside objects

# 1--------
class Teacher:
    def __init__(self, name):
        self.name = name

# 2------
class Course:
    def __init__(self, name , teacher):
        self.name = name
        self.teacher = teacher

#3--------

teacher1 = Teacher("Ulf")

course1= Course("Python", teacher1)

#4

print(course1.name, course1.teacher.name)




