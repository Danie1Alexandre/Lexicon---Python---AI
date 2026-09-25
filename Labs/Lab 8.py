# Part A - Mutable default arguments

#1 --------

# class BadTeam:
#     def __init__(self, name, members = []): #bad
#         self.name = name
#         self.members = members 

#     def add_member(self,member):
#         self.members.append(member)

# #2------
# club1 = BadTeam("aik")
# club2 = BadTeam("dif")

# club1.add_member("anna")

# print(club1.members) 
# print(club2.members)
# # anna added on both clubs, since both clubs uses the same list

# # 3---------------

# class GoodTeam:
#     def __init__(self, name, members = None): #bad
#         self.name = name
#         if members == None:
#             members = []
            
#         self.members = members

#     def add_member(self,member):
#         self.members.append(member)

# #4A--------------
# club1 = GoodTeam("aik")
# club2 = GoodTeam("dif")

# club1.add_member("anna")

# print("good", club1.members) 
# print(club2.members)



# Part B - Dictionary or class?
#1
# movie ={
#     "title": "Blade Runner",
#     "director" :"Ridley Scott",
#     "rating" : 4
# }
# # #2
# class Movie:
#     def __init__(self, title, director, rating ):
#         self.title = title
#         self.director = director
#         self.rating = rating
            
# movie_BR = Movie("Blade Runner", "Ridley Scott", 4)

# print(movie_BR.rating)

# #3
# class Movie:
#     def __init__(self, title, director, rating ):
#         self.title = title
#         self.director = director
#         self.rating = rating

#     def highly_rated(self):
#         if self.rating > 3:
#             return "The Movie Is Higly Rated"
            
# movie_BR = Movie("Blade Runner", "Ridley Scott", 4)

# print(movie_BR.rating)
# print(movie_BR.highly_rated())

# #4

# #for simpel info i use dictionary. a product list
# #if the dictionary needs to do something , "have a method",  then class is better 

# # Part C - Inheritance fundamentals

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
        
# account1 = Account("anna", 1200)
# account2 = SavingsAccount("ben", 1000, 0.03)

# print(account1.owner, account1.balance)
# print(account2.owner, account2.balance, account2.interest_rate)

# 5 
# "is-a" statement:
# A SavingsAccount IS-A type of Account.

# Part D - Inherited and subclass-specific behaviour
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return "my info"
    
class Developer(Employee):
    def my_statues():
        return "online"

class Maneger(Employee):
    def say_hello(self):
        return "Hello"


developer = Developer("john")
maneger = Maneger("bob")

print(developer.get_information)

# #Part F - Method overriding

# class Notification:
#     def send():
#         return("this is a message")

# class EmailNotification(Notification):
#     def send():
#         return("this is a email message")
# class SMSNotification(Notification):
#     def send():
#         return("this is a sms message")

# vanilla = Notification
# email = EmailNotification
# sms = SMSNotification

# print(vanilla.send()) # using method from base class
# print(email.send()) #using method from EmailNotification
# print(sms.send()) #using method from smsNotification

#Part G - Override and still use the base method

class Report:
    def get_summary(self):
        return "summary"
    
class SalesReport(Report):
    def get_summary(self):
        base_info = super().get_summary()
        return f"sales {base_info}"
    
sales = SalesReport()    
print(sales.get_summary())


# # Part H - Applied challenge: User accounts
# # H1 and 2

# class User:
#     def __init__(self, username, email, age):
#         self.username = username
#         self.email = email
#         self.active = True
#         self.age = age
#         if self.age < 0:
#             raise ValueError("age cannot be negative!")

#     def say_hello(self):
#         return "Hello im a user"
    


# #H3
#     def change_email(self,email):
#         self.email = email


# #H4

# class AdminUser(User):
#     def __init__(self, username, email, age):
#         super().__init__(username,email,age)
     
#         self.user_list = []

#     def delete_user(self, user):
#         self.user_list.remove(user)

#     def add_user(self, user):
#         self.user_list.append(user)

#     def say_hello(self):
#         base_text = super().say_hello()
#         return f" {base_text} and a Admin"



# class PremiumUser(User):

#     def __init__(self, username, email, age):

#         super().__init__(username,email,age)    
#         self.premium = "I got premium"
    
#     def emote(self):
#         print(self.username, "=)")

#     def say_hello(self):
#         return "Hello im a premium user"

# user2 = PremiumUser("Lisa", "lisa@mail.com", 17)
# print(user2.username, user2.email, user2.premium)
# user2.emote()


# #H5

# user3 = AdminUser("ben", "admin@mail.com", 21)
# print(user3.username, user3.email,)


# user1 = User("Anna", "anna@mail.com", 24)
# print(user1.username, user1.email)

# #6
# print(user1.username, user1.say_hello())
# print(user2.username, user2.say_hello())
# print(user3.username, user3.say_hello()) #7

# #8

# print("old email", user2.email)
# user2.change_email("l.new@mail.com")
# print("new email", user2.email)

# user3.add_user("smeagol")
# print("admins user list",user3.user_list)
# user3.delete_user("smeagol")
# print("admins user list, empty aftre delte",user3.user_list)

# print(user1.say_hello())
# print(user2.say_hello())

# #9
# print(user2.age)
# print(user3.age)




#10 admin and premium user is a user of the app, therefor they belongs to user class




