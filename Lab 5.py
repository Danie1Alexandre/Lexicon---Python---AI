def print_separator():
     print("_"*40)

# Part A - Scope


#1

course_name = "python"

def courses():
    course_name = "Ai"
    print(course_name)


courses() #prints a local variabel
#specifik for the function couses

print(course_name) #prints a Global variabel

print_separator()


#2
count = 0 #Global

def counter():
    count = 0 # Local
    count += 1
    print (count)

#same variabel name but count stay on zero on golbal
    
counter()
print(count)

#3

greet = "hello"
name = "ada"


def name_format(Name):
    greet = "Good Day"
    print(name, greet)

name_format(name)
print(greet)





   



