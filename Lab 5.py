
# Part A - Scope

#1

# course_name = "python"

# def courses():
#     course_name = "Ai"
#     print(course_name)


# courses() #prints a local variabel
# #specifik for the function couses

# print(course_name) #prints a Global variabel




# #2
# count = 0 #Global

# def counter():
#     count = 0 # Local
#     count += 1
#     print (count)

# #same variabel name but count stay on zero on golbal
    
# counter()
# print(count)

#3

# score = 10  #global

# #there will be a error
# #the function dont have a value for score
# def add_score():  
#     score +=1
#     print("score")
# #add_score()

# #solution
# def new_add_score(score):  
#     return score + 1

# print (new_add_score(score))




#4

def function_one():
    this_is = "first function"

    def function_two():
        #"enclosing-scope lookup" second function can use Variables from the first function 
        # in nessted function
        print(this_is)
    
    function_two()

function_one()

#5 

# numbers = [1, 2, 3]
# # sum = 10 
# #python crashes beacuse variable sum is shadowing built in function sum
# total = sum(numbers)

# #soultion
# _sum = 10  # rename sum to something else
# total = sum(numbers) + _sum
# print(total)


#part B - *args

#1B-------------

def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_all(1, 3, 8))

#2B-----

def average(*numbers):
    if len(numbers) == 0:
        return None
    
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

print(average())

#3B----------

def longest_word(*words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(longest_word("apple", "banana", "computer", "python", "galaxy"))
      

#4B

def build_sentence(separator, *words):
    return separator.join(words)

print(build_sentence(", ","apple", "banana", "computer", "python", "galaxy"))

#5B

def describe_scores(student_name, *scores):
    if len(scores) == 0:
         return student_name, 0, 0 
  
    
    score_lenght = len(scores)
    total = 0

    for score in scores:
        total += score

    average = total/len(scores)

    return student_name, score_lenght, average

print(describe_scores("noa", 4, 6, 8, 2))

# part C - Postional unpacking

#1c ------- 
positinal_numbers_list = [10, 20, 30]

def positinal_numbers(a,b,c):
    print(a,b,c)

positinal_numbers(*positinal_numbers_list)

#2c --------

info =("adrian","gunther", "Berlin")

def person_info(fist_name,last_name,city):
    print(fist_name, last_name, city)

person_info(*info)

#3C----------------
def unpacking(values):#unpacking 
    print("original list", values)

    first, *middle, last = values

    print("first", first)
    print("middle", middle) #starred assignment
    print("last",last)

unpacking([1, 2, 3, 4, 5])
unpacking(["A", "B", "C", "D", "E","F", "G"])

#4-------

# In a function definition, * lets the function accept
# an unknown amount of arguments.
def print_scores(*scores):
    print(scores)

# In a function call, * unpacks a collection to send
# an unknown amount of arguments.
my_list = [10, 20, 30]
print_scores(*my_list)

#Part D - ** kwargs













# Part G- Stretch challenges
#1 

# def merge_settings(defaults, **overrides):

#     return {**defaults, **overrides}

# default_settings = {"theme": "light", "volume": 50, "show_notifications": True}

# user_settings = merge_settings(default_settings, theme="dark", volume=75)

# print("Original defaults:", default_settings)
# print("New merged settings:", user_settings)






   



