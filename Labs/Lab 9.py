#Part A - Polymorphism

class PushNotification:
    def send(self):
        return("this is a push message")

class EmailNotification:
    def send(self):
        return("this is a email message")
class SMSNotification:
    def send(self):
        return("this is a sms message")

Notification_list = [PushNotification(),EmailNotification(), SMSNotification()]

for notification in Notification_list:
    print(notification.send())

#all objects have a send method, so there is no need too name the exact class.

# Part B - Polymorphism with inheritance

class Document:
    def __init__(self, title):
        self.title  = title

    def describe(self):
        return("generic document")

class PDFDocument(Document):
    def describe(self):
        return("PDF document")

class TextDocument(Document):
    def describe(self):
        return("text document")

text1= TextDocument("tex1")
text2= TextDocument("tex2")
text3= TextDocument("tex3")

pdf1 = PDFDocument("pdf1")
pdf2 = PDFDocument("pdf2")
pdf3 = PDFDocument("pdf3")

documnets = [text1, text2, text3, pdf1, pdf2, pdf3]

for document in documnets:
    print(f"Title: {document.title} - Description: {document.describe()}")

# Part C - Duck typing

class Printer:
    def display_status(self):
        return("my Printer status")

class Screen:
    def display_status(self):
        return("my Screen status")

printer = Printer()
screen = Screen()

hardwears = [printer, screen]

for hardwear in hardwears:
    print (hardwear.display_status())
    
#all objects have a display_status method, so there is no need too name the exact class.
#classes dosent have too be in same baseclass for Duck typing

#Part D - isinstance()

class User:
    def __init__(self, username):
        self.username = username


class AdminUser(User):
    def __init__(self, username):
        super().__init__(username)
     
user3 = AdminUser("ben")

print(isinstance(user3,User))
print(isinstance(user3,AdminUser))
print(isinstance(user3,str))

#A user can be a admin, so a admin is also a user


