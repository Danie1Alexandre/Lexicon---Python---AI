# Part A - Conditions
#-----------------------------
# A1 ------
#num = int(input("type a number"))
# num = 17
# if num < 0:
#     print("negative")
# elif num > 0:
#     print ("positive")
# else:
#     print("zero")    

# # 2-------------------------
    
# age = int(input("type a age"))

# if age < 20:
#     print("less then 20")
# elif age >= 20 and age <=30 :
#     print("bettwen 20- 30")
# elif age >= 31 and age <=40 :
#     print("bettwen 31- 40")
# else:
#     print("above 40")

#3---------------------

# user = input("type username")
# passcode = input("type password")


# user_name = "bob"
# password= "123"

# if user == user_name and passcode == password:
#     print("password match")
# else:
#     print ("wrong password or username") 

#4
# score = int(input("type a score"))

# if score <= 10 :
#     print("Grade E")
# elif score <= 20:
#     print("Grade D")
# elif score <= 40 :
#     print("Grade C")
# elif score <= 60 :
#     print("Grade B")
# elif score > 60:
#     print("Grade A")

#5--------------

# member = "yes"
# total_order = 300


# if member == "yes" and total_order >= 300:
#     print("free_shipping") 
# else:
#     print("shipping fee is 50")

#6------------

# print(7==7) #true
# print(9 != 9) #false
# print(7 > 5) #true
# print(9 <= 7) #false
# print( 10 <= 10) #true

# Part B - Truhy, Falsy and mebership
#----------------------------

#B1-------------------

# empty_string = ""
# if empty_string:
#     print("not empty")
# else:
#     print("empty")

# string = "x"
# if string:
#     print("not empty")
# else:
#     print("empty")

# zero = 0
# if zero:
#     print("not empty")
# else:
#     print("empty") #its empty

# zero = 1
# if zero:
#     print("not empty") #not empty
# else:
#     print("empty") 

# test_list = ""
# if test_list:
#     print("not empty")
# else:
#     print("empty") #its empty

# test_list = "yo"
# if test_list:
#     print("not empty") #not empty
# else:
#     print("empty") 

# B2 ------------------------

# languages = ["Python", "JavaScript", "C++", "Java"]
# language = "Python"

# if language in languages:
#     print("in the list" )
# else:
#      print("not in the list" )

#B3----------------
# blocked_names = ["Alice", "Liam", "Maja", "Noah"]
# blocked_name = "Alice"

# if blocked_name in blocked_names:
#     print("user blocked" )

#B4-------------
# is_logged_in = False
# is_a_member = False

# #not reverse the boolean, since the variables are false-
# #the if stament becomes true when using not. "not false"
# if not is_a_member and not is_logged_in: 
#     print("user it not looged in and not a meber")
# else:
#     print("user is a logged in member")



# Part C - For loops
#--------------------------------------------

#c1---------------
# names = ["Alice", "Liam", "Maja", "Noah"]
# Hello = "hello"
# number = 1
# for name in names:
#     print(number,Hello, name)
#     number +=1

#c2----------------------------

# nr_list = list(range(1, 51))

# for number in nr_list:
#     if number % 2 == 0: 
#         print("even", number)

#C3----------------
# total = 0
# for number in nr_list:
#     total = number + total 
# print(total)

#C4---------------
# number_list = [1, 2, 3,  25,336, 37, 3800, 5, 46, 47, 48, 49, 50]
# largest_number = 0
# for number in number_list:
#     if number > largest_number:
#         largest_number = number
# print(largest_number)

#C5----------------

# languages = ["Python", "JavaScript", "C++", "Java"]
# word_biger_then_5 = 0

# for lang in languages:
#     if len(lang) > 5:
#         word_biger_then_5 +=1
# print(word_biger_then_5)

#C6-------------

# scores =[10, 34, 86, 73, 45, 23]
# passes = 0
# failed= 0

# for score in scores:
#     if score >= 70:
#         passes +=1
#     elif score < 70:
#         failed +=1
# print("passes: ", passes," failed:", failed)

#C7------------------

student = {
    "name" : "ada",
    "age" : 24,
    "course" : "AI",
    "course2" : "Python"
}

for key in student.keys():
    print(key)

for values in student.values():
    print(values)

for item in student.items():
    print(item)

    
# Part D - Range, enumerate and nested loops
#D1----------------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in range(10,0,-1):
#     print(number)

#D2------------------------

# number_to_multipli = int(input ("number to multipli "))

# for num in range(11):
    
#     output = num*number_to_multipli

#     print(number_to_multipli, " x ", num, " = ", output)

#D3-------------

# songs = [
#     "Blinding Lights",
#     "Shape of You",
#     "Bohemian Rhapsody",
#     "Billie Jean",
#     "Stayin' Alive",
#     "Hotel California",
#     "Rolling in the Deep",
#     "Dance Monkey",
#     "Smells Like Teen Spirit",
#     "Hey Jude"
# ]

# for index, song in enumerate(songs,start=1):
#     print(index, song)

#D4-------------------

# for x in range(1,5):
#     for y in range(1,5):
#         print("X", x,"Y",y)

#D5----------------

# print("grid")
# for row in range(5):
#     for colum in range(5):
#         print("x",end="") #enkel grid
#         #print(f"{row}:{colum}", end=" ") # för koordinater
#     print()

# E - while loops
#--------------------------------

# E1---------
# countdown = 10  
# import time  
# while countdown > 0:
#     print(countdown)
#     time.sleep(0.5)
#     countdown -=1
# print ("boom!, rocket lunched") # =)

# E2---------------

# password = "123"
# userinput = ""

# while userinput != password:
#     userinput= input("type password ")

# print("password correct")

# E3-----------------

# option_1 = "1 game"
# option_2 = "2 email"
# option_3 = "3 quit"

# menu = [1, 2, 3]
# user_option = 0

# while user_option != menu[2]:
#     print(option_1, option_2, option_3)
#     user_option = int(input("pick a number "))

#     if user_option == 1:
#         print("user picked", option_1)
#     elif user_option == 2:
#         print("user picked", option_2)
#     elif user_option == 3:
#         print("user picked", option_3)
#     else:
#         print ("pick a number betwen 1-3")
#     print()

# E4-------------------

# total = 0
# user_input = None

# while user_input != 0:
#     user_input= int(input("pick a number, 0 to quit "))
#     total += user_input
# print("total", total,)

# E5--------------------

# secret_number = 67
# user_input = None
# while user_input != secret_number:
#     user_input= int(input("Guess the secret number"))
#     if user_input != secret_number:
#         if user_input > secret_number:
#             print("Number is to high, Guess again")
#         else:
#             print("Number is to low, Guess again")
#     else:
#         print("Correct, secret number was:", secret_number)

# Part F- break and continue
#---------------------------------------

#F1----------------
# numbers_1000 = list(range(1, 1000))

# for number in numbers_1000:
#     if number % 7 == 0 and number % 9 == 0:
#         print("First number divisible by both 7 and 9 is:", number)
#         break

#F2----------

# songs = [
#     "Blinding Lights",
#     "Shape of You",
#     "",
#     "Billie Jean",
#     "Stayin' Alive",
#     "",
#     "Rolling in the Deep",
#     "Dance Monkey",
#     "Smells Like Teen Spirit",
#     "Hey Jude"
# ]

# for song in songs:
#     if song == "":
#         continue
#     print(song)

#F3----------

# search_name =["Alice", "Liam", "Maja", "Noah"]

# tragetd_name = "Maja"
# found= False 
# # If the name is found, found becomes true.
#  # Otherwise, if False the name was not found.

# for name in search_name:
#     if name == tragetd_name:
#         found= True
#         print ("found name")
#         break

    
# if not found:
#     print("name not in list")

#F4 ----------

# mixed_numbers =[ 7, -3, 5,-10,999, 23, 34]

# for number in mixed_numbers:
#         if number < 0:
#             continue
#         elif number ==999:
#             break
#         print (number)
    
# part G Applied challenge: Console study tracker

#G1  ------------
# study_sessions= [
#     {"subjects": "math", "minutes": 45},
#     {"subjects": "python", "minutes": 59},
#     {"subjects": "swedish", "minutes": 50},
#     {"subjects": "math", "minutes": 57},
#     {"subjects": "python", "minutes": 53},
#     {"subjects": "swedish", "minutes": 120},
#     {"subjects": "swedish", "minutes": 34},
#     {"subjects": "math", "minutes": 30},
#     {"subjects": "math", "minutes": 40},
#     {"subjects": "python", "minutes": 55}
# ]


#G4---------------------
# longest_session= None
# longest_time = 0

# for session in study_sessions:
#     if session["minutes"] > longest_time:
#         longest_time = session["minutes"]
#         longest_session=session
# print(longest_time)
# print(longest_session)

#G5-----------------

# for session in study_sessions:
#     if session["minutes"]> 45:
#         print(session)



# #g6-G7----------------
# import time

# while True:
#     print("\n--- MENU ---")
#     print("1: view all sessions")
#     print()
#     print("2: view total time, ")
#     print()
#     print("3: filter by subject, ")
#     print()
#     print("4: Quit")

#     user_input = int (input("pick a number: "))
    

#     if user_input == 4:
#         break

#     elif user_input == 1:
#         for session in study_sessions:
#             print(f"Subject: {session['subjects']}, Minutes: {session['minutes']}")
#         time.sleep(1)

#     elif user_input == 2:# G2 ------------
#         total_minutes = 0

#         for session in study_sessions:
#             total_minutes += session["minutes"]
#         print(total_minutes)
#         time.sleep(1)

#     elif user_input == 3: #G3------------

#         total_minutes_in_subjects = {}

#         for session in study_sessions:
#             subject=session["subjects"]
#             minutes =session["minutes"]

#             if subject in total_minutes_in_subjects: #if true existera redan
#                 total_minutes_in_subjects[subject] += minutes
#             else:
#                 total_minutes_in_subjects[subject] = minutes

#         print(total_minutes_in_subjects)
#         time.sleep(1)
        
# Part H - Strech challenges

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz")    
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)

# sentence = "Python programming is fun"
# vowels = "aeiouyAEIOUY"
# count = 0

# for char in sentence:
#     if char in vowels:
#         count += 1 

# print(count)

# numbers = [1, 2, 3, 2, 4, 5, 3, 2]
# seen = []
# duplicates = []

# for number in numbers:
#     if number in seen:
#         if number not in duplicates:
#             duplicates.append(number)
#     else:
#         seen.append(number)

# print(f"duplicates: {duplicates}")

# numbers = [3,5,2]

# for number in numbers:
#     print("*"*number)