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