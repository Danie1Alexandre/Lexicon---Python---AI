#part A - List Comprehensions
#1
Numbers = list(range(1, 21)) 
squared_numbers=[]

for number in Numbers:
    squared_numbers.append(number ** 2) # ** power of
print("normal", squared_numbers)

squared_comprehension = [number ** 2 for number in Numbers]

print("com", squared_comprehension)

#2

even_numbers = [number for number in range(1, 101) if number % 2 == 0]

print(even_numbers)


#3

names = [ "alice", "liam", "maja"]

title_names = [name.strip().title() for name in names]

print(title_names)

#4


scores = [45, 88, 92, 31, 75, 60, 49, 95]

passing_scores = [score for score in scores if score >= 70]

print(passing_scores)

# 5

pass_or_fail = ["PASS" if score >= 70 else "FAIL" for score in scores]

print(pass_or_fail)

#6

languages = ["Python", "JavaScript", "C++", "Java"]
# word_biger_then_5 = 0

# for lang in languages:
#     if len(lang) > 5:
#         word_biger_then_5 +=1
# print(word_biger_then_5)

word_biger_then_5 = [langue for langue in languages if len(langue) > 5]
print(word_biger_then_5)
print(len(word_biger_then_5))

study_hours = {
    "Math": 15,
    "Python": 25,
    "English": 10,
}

# total_hours_loop = 0
# for hours in study_hours.values():
#     total_hours_loop += hours

# print("Total:", total_hours_loop)

study_hours_total= sum ([hour for hour in study_hours.values()])

print(study_hours_total)

# score = int(input("type a score"))
scores =[10, 34, 86, 73, 45, 23]
# passes = 0
# failed= 0

# for score in scores:
#     if score >= 70:
#         passes +=1
#     elif score < 70:
#         failed +=1
# print("passes: ", passes," failed:", failed)

score_pass = len([score for score in scores if score >=70])
score_fail = len([score for score in scores if score <70])

print("passes: ", score_pass, " failed:", score_fail)

# Part B - Dictionary and set comprehensions

#1 

squares_dictionary = {number: number**2 for number in range(1,11)} 
print(squares_dictionary)

#2
words = [
    "apple", "banana", "computer"
]

word_lenght = {word: len(word) for word in words}
print(word_lenght)

#3

set_words = [
    "Apple", "BANana", "coMPuter, apple, banana, Computer"
]

word_lower = {word.lower() for word in set_words}
print(word_lower)

#4

products = {
    "apple" : 5, 
    "banana" : 8, 
    "computer" : 20,
     "coffee" : 7, 
     "guitar" : 15, 
     "window" : 10
}

below_products = { product: price for product, price in products.items() if price < 10 }
print(below_products)

#5

students = [
    {
        "name": "alma",
        "score" : 75   
    },

    {
        "name":"bert",
        "score" : 55   
    }
]

student_status = {student["name"]:"pass" if student["score"] >= 70 else "fail" 
                  for student in students
                  }

print(student_status)

#part C enumarate

#1
songs = [
    "Blinding Lights",
    "Shape of You",
    "Bohemian Rhapsody",
    "Billie Jean",
    "Stayin' Alive",
    "Hotel California",
    "Rolling in the Deep",
    "Dance Monkey",
    "Smells Like Teen Spirit",
    "Hey Jude"
]

for index, song in enumerate(songs,start=1):
    print(index, song)


# 2
    
tasks = [
    "Buy groceries",
    "Clean the kitchen",
    "Answer emails",
    "Study Python",
    "Go for a run"
]
    
for index, task in enumerate (tasks, start=1):
    print(f"Task {index}: {task}")

# 3 
scores =[10, 34, 86, 73, 45, 23]
threshold = 40

value_above_treshold = [index for index , score in enumerate (scores, start = 1 ) if score > threshold]
print(value_above_treshold)

#4

fruits = ["apple", "banana", "orange"]

for fruit_index in range(len(fruits)):
    fruit = fruits[fruit_index]  
    print(fruit_index, fruit)

for index, fruit in enumerate(fruits): 
    # A simple enumerate is slightly shorter/more readabel code then for loop
    # 1 line of code vs 2
    print(index, fruit)

#part D zip and unpacking

#1---------------
fruits = ["apple", "banana", "orange"]
scores =[10, 34, 86, ]

for fruit, score in zip(fruits, scores):
    print(fruit,score)

#2----------------

fruit_score = {fruit: score for fruit, score in  zip(fruits, scores) }
print(fruit_score)
print (type(fruit_score))

#3-------

names = ["Laptop", "Smartphone", "Headphones", "Keyboard"]

prices = [8999, 4999, 799, 450,456]

stocks = [12, 25, 0, 8]

for name,price, stock in zip( names, prices, stocks):
    print("name: ", name,"price: ", price, "stock", stock)

#catalog = {"product": "name", "prices": 0, "stock": 0 for "product": "name", "prices": 0, "stock":}

# 4 -------
#if you add extra itmes in one list, does extra values will be ingnored
#or you could say only the lenght of the shortest list will be used
prices_ex = [8999, 4999, 799, 450,456] # 5 values

stocks_ex = [12, 25, 0, 8] # 4 values

#5-----------

for name, price in zip(names, prices):
    print(f"Product: {name}, Price: {price}")

#6 ---------
A = 10
B = 55
print(A, B)
A, B = B, A
print(A, B)


