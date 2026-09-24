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
