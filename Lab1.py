#warm-up

#A1
# name = "daniel"
# course = "Python"
# study_goal = "warm-up: python basic"

# print(name)
# print(course)
# print(study_goal)

# #A2
# name = "anna"
# age = 30
# height_in_meters = 1.6
# is_student = True

# print(name)
# print(age)
# print(height_in_meters)
# print(is_student)

# print(type(name))
# print(type(age))
# print(type(height_in_meters))
# print(type(is_student))

# #A3
# year = 2026
# print(type(year))

# year = "2026"
# print(type(year))

# #python is dynamically typed 
# """You can change a variable to different types; 
# it is not locked to one specific type."""

# #A4

# A = 5
# B = 2

# print(f"{A} + {B} =", A+B)
# print(f"{A} - {B} =", A-B)
# print(f"{A} x {B} =", A*B)
# print(f"{A} / {B} =", A/B)
# print(f"Floor division, [{A} / {B}] =", A//B)
# print(f"To the power of, {A} ^ {B} =", A**B)

# #A5

# string_num = 10
# num =  10
# convert_to_int = int(string_num)
# print("10 + 10 =", num + convert_to_int)

# B = 11
# print(type(B), B)
# convert_to_float = float(B)
# print(type(convert_to_float), convert_to_float)

# num3 = 12
# string = "number is: " 
# convert_to_string = str(num3)
# add_string = string + convert_to_string
# print(add_string)

# # User input and calculation

# #1B
# from datetime import datetime

# name = input("What is your name? ")
# year_of_birth = int (input("what is your birth year? "))

# current_year = datetime.now().year
# age = current_year - year_of_birth

# print ("your name:",name, "age:",age)

# #2B
# price = int (input ("how much does your iteam coast"))
# discount = int (input ("how much is the discount in percentage"))
# discount_in_number = price * discount / 100
# final_price = price -discount_in_number
# #final_price = price * (1 - discount / 100) alternativ

# print(final_price)

# #3B
# celsius = int (input ("what is the temprature in celsius"))
# F = celsius*9/5+32
# print("temprature in fahrenheit: ", F)

# #4B
# lenght = int (input ("what is the lenght"))
# width = int (input ("what is the width"))

# area = lenght*width
# perimeter = 2*(lenght+width)

# print("area is:", area, "perimeter is:", perimeter)

# #5B
# # users needs to enter correct value-type 
# # python will give a valueError if wrong value is used. 
# #  e.g. if python ask for a number
# # and the user trys to enter a letter instead of a number/int
# # it will not work, basiclly the program will crash

#part C - Strings

# #1---
# Hello = " Hello world im calling from space "

# print(len(Hello))

# print(Hello.upper())
# print(Hello.lower())
# print(Hello.strip())

# #2---

# first_name = "bert"
# lastname = "bertson"

# print(f" {first_name} {lastname}")

#3

# pp= "python programming"

# print(pp[0])
# print(pp[-1])
# print(pp[:6])
# print(pp[7:])
# print(pp[::-1])

#4
# user_input = input("type first name")
# first_name = user_input

# user_input = input("type last name")
# last_name = user_input

# first_name = first_name.strip().lower()
# last_name = last_name.strip().lower()
  
# user_name = first_name[:3] + last_name[:5]

# print(user_name)

#5

# email= "exmpel@mega.com"

# split_email = email.split("@")

# user = split_email[0]
# domain= split_email[1]

# print(user, domain)

#6

# sentence = "this is java"

# sentence2 =  sentence.replace("java", "python")
# print(sentence)
# print(sentence2)

#part D string investigation

#1D

# text="paradise"
#                 #prediction
# print(text[1]) # a
# print(text[-1]) # e
# print(text[1:5]) # arad
# print(text[:3]) # par
# print(text[5:]) # ise
# print(text[:-4]) # dise
# print(text[-6:]) # ise
# print(text[0:6:2]) # prds

# #2D

# text2 ="Artifical Intelligence"
#                 #name
# print(text2[1]) # psoitive index
# print(text2[-1]) # negative index
# print(text2[0:len(text2)]) # slicing
# print(text2[:3]) # omitted start
# print(text2[5:]) # omitted end
# print(text2[:-4]) # negative index slicing
# print(text2[-6:]) # negative index slicing
# print(text2[0:6:2]) # slicing with steps

#3D

# data = "apple, banana, mango"

# print(data)
# print(data.split(","))
# # the string becomes  a list"

# space= "       huge.space"

# print(space)
# print(space.strip())
# #removes unwanted space in strings

# sentence = "this is java"
# print(sentence)
# print (sentence.replace("java", "python"))
# #replace a word in a string

# email= "exmpel@mega.com"

# if "@"in email:
#     print("this is a email")

# # in check if a letter is used in the string

#4D

# word= "Dog"

# #word[0]= "j"# dont work
# word = "j" + word[1:] #chnage the lette on immutable
# print (word)

# #part E applied challenge: Registration summary

# #1E
# first_name = input("type first name")

# last_name  = input("type last name")

# birth_year = (input("type birth year"))

# fav_pr_lang = (input("type programming language"))


# #2

# first_name = first_name.strip()
# last_name = last_name.strip()

# #3
# user_name = first_name[:3] + last_name[:5] + birth_year[0]

# #4
# print(f" {first_name} {last_name} {fav_pr_lang} {user_name}")

# #5

# full_name= first_name + last_name
# print(full_name)
# print(f" {first_name[0]} {last_name[0]} {len(full_name)}  {fav_pr_lang[::-1]}")

# #6
# print(first_name[:3]) # omitted start

# print(f" {first_name[0]} {last_name[0]} {len(full_name)} {fav_pr_lang[::-1]} {first_name[:3]} {first_name[::2]} {first_name[1:3]}")

#part F - Strech challenges Python Foundation

#1
# seconds= int (input("type seconds"))
# hour_left = seconds// 3600
# print (hour_left)

# remaining_seconds = seconds% 3600
# print (remaining_seconds)

# minutes = remaining_seconds//60

# second= remaining_seconds%60

# print(f"{hour_left} timmar, {minutes} minuter och {second} sekunder.")


#2F

number = 1818

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

# Skriv ut varje siffra
print(thousands)
print(hundreds)
print(tens)
print(ones)

# 3F -------------

word = "windows"
hidden_text = ""

for position  in range (len(word)):
    if position  > 1 and position  < len(word) -2:
        hidden_text += "*"
    

hidden_word = word[:2] + hidden_text + word[-2:]

print(hidden_word)

# 4F

word = "windows"
print(word[3:])

word = "windows"
print(word[:-4])

x = 4
y = "7"
print(x+ int (y))

number = 55
print(number % 10 + number // 10)

a = "13"
b= "37"
print(a+b)
