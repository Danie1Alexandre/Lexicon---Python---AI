
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

score = 10  #global

#there will be a error
#the function dont have a value for score
def add_score():  
    score +=1
    print("score")
#add_score()

#solution
def new_add_score(score):  
    return score + 1

print (new_add_score(score))




#4




# Part G- Stretch challenges
#1 











   



