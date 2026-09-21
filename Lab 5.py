
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


# Part G- Stretch challenges
#1 

# def merge_settings(defaults, **overrides):

#     return {**defaults, **overrides}

# default_settings = {"theme": "light", "volume": 50, "show_notifications": True}

# user_settings = merge_settings(default_settings, theme="dark", volume=75)

# print("Original defaults:", default_settings)
# print("New merged settings:", user_settings)






   



