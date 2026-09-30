def print_separator():
     print("_"*40)

def pick_food(food):
     print("\n================ Food ================")
     print("1.", food[0])
     print("2.", food[1])
     print("3.", food[2])
     print("========================================")

# def feed_animals(animal_type)


def take_user_input():
     import time
     x = 1

     while x == 1:
          user_input = input("pick a number \n")
          
          if user_input == "1":
               return user_input
               x = 0
          elif user_input == "2":
               return user_input
               x = 0
          elif user_input == "3":
               return user_input
               x = 0
          elif user_input == "4":
               return user_input
               x = 0
          
          else:
               print("Not a valid option") #handel user input error
               time.sleep(1)
