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

# Part E - __str__

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        

product1 = Product("apple", 5)
print(product1)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - price: {self.price}"
                
product1 = Product("apple", 5)
product2 = Product("banana", 10)
product3 = Product("mango", 14)
print(product1)
print(product2)
print(product3)

store =str(product3)
print(store)
print(type(store))

#Part F - __str__ with inheritance

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} - {self.balance}"
    
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def __str__(self):
        return f"{self.owner} - {self.balance} - {self.interest_rate}"        

account1 = Account("anna", 1200)
account2 = SavingsAccount("ben", 1000, 0.03)

print(account1)
print(account2)

# Part G - Inheritance or composition?

class CPU:
    def __init__(self, model):
        self.model = model

class Computer:
    def __init__(self, brand, cpu):

        self.cpu = cpu
        self.brand = brand

cpu = CPU("intel")

computer = Computer("msi", cpu)

print(computer.brand)
print(computer.cpu.model)

#a cpu us is not a computer but a computer has a cpu


#car Has a engine 
# Manger is a employee
# Course has a teacher
#Phone is a dvice

#Part H - Applied challenge: Export system
data_input = "python data"
class Exporter:
    def __init__(self, name):
        self.name = name
    
    def export(self, data):
        return("data exported:", data)
   
    def __str__(self):
        return f"{self.name}"  
        
class ConsoleExporte(Exporter):
    def export(self, data):
        return("console exported:", data) 
    
class TextExporter(Exporter):
    def export(self,data):
        return("text exported:", data)
    

class SummaryExporter(Exporter):
    def export(self, data):
        return("summary exported", data)

data = Exporter("d1")   
console = ConsoleExporte("C1")
text = TextExporter("T1")
summary = SummaryExporter("s1")


class Printer:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def __str__(self):
        return f"{self.name} - {self.model}"

    def export(self, data):
        return("printer exported", data)
    
class Laser:
    def __init__(self, model):
        self.model = model
    def __str__(self):
        return f"{self.model}"

laser = Laser("HP_Laser")

printer = Printer("p1", laser)

export_list = [console, text, summary, data, printer]
for export in export_list:
    print(export.name,export.export(data_input))

print(isinstance(summary,SummaryExporter))

print(printer)

# Composition: Printer HAS-A Laser
