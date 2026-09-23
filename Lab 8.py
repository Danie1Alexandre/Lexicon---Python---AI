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
movie ={
    "title": "Blade Runner",
    "director" :"Ridley Scott",
    "rating" : 4
}
# #2
# class Movie:
#     def __init__(self, title, director, rating ):
#         self.title = title
#         self.director = director
#         self.rating = rating
            
# movie_BR = Movie("Blade Runner", "Ridley Scott", 4)

# print(movie_BR.rating)

#3
class Movie:
    def __init__(self, title, director, rating ):
        self.title = title
        self.director = director
        self.rating = rating

    def highly_rated(self):
        if self.rating > 3:
            return "The Movie Is Higly Rated"
            
movie_BR = Movie("Blade Runner", "Ridley Scott", 4)

print(movie_BR.rating)
print(movie_BR.highly_rated())

#4

#for simpel info i use dictionary. a product list
#if the dictionary needs to do something , "have a method",  then class is better 

# Part C - Inheritance fundamentals

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        
account1 = Account("anna", 1200)
account2 = SavingsAccount("ben", 1000, 0.03)

print(account1.owner, account1.balance)
print(account2.owner, account2.balance, account2.interest_rate)

# 5 
# "is-a" statement:
# A SavingsAccount IS-A type of Account.

#Part F - Method overriding

class Notification:
    def send():
        return("this is a message")

class EmailNotification(Notification):
    def send():
        return("this is a email message")
class SMSNotification(Notification):
    def send():
        return("this is a sms message")

vanilla = Notification
email = EmailNotification
sms = SMSNotification

print(vanilla.send()) # using method from base class
print(email.send()) #using method from EmailNotification
print(sms.send()) #using method from smsNotification


# Part H - Applied challenge: User accounts
# # H1 and 2

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#         self.active = True

# #H3
#     def change_email(self,email):
#         self.email = email

# user1 = User("Anna", "anna@mail.com")
# print(user1.username, user1.email)

# #H4

# class AdminUser(User):
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email        

#         self.user_list = []

#     def delete_user(self, user):
#         self.user_list.remove(user)



# class PremiumUser(User):

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email        
#         self.premium = "I got premium"
    
#     def emote(self):
#         print(self.username, "=)")

# user2 = PremiumUser("Lisa", "lisa@mail.com")
# print(user2.username, user2.email, user2.premium)
# user2.emote()


# #H5

# class AdminUser(User):
#     def __init__(self, username, email):
#         super().__init__(username,email)

#         self.user_list = []

#     def add_user(self, user):
#         self.user_list.append(user)


# class PremiumUser(User):

#     def __init__(self, username, email):
#         super().__init__(username,email)

#         self.premium = "I got premium"
    
#     def emote(self):
#         print(self.username, "=)")

# #6



