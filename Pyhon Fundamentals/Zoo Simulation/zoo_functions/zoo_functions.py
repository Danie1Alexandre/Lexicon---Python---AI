import sys
import time

def print_separator():
     print("_"*40)

def pick_food(food):
     print("\n================ Food ================")
     print("1.", food[0])
     print("2.", food[1])
     print("3.", food[2])
     print("========================================")

# def feed_animals(animal_type)


def take_user_input(): #handel user input error
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
               print("Not a valid option")
               time.sleep(1)

def end_game_condition(animals):
     for animal in animals:        
          if animal.health < 1:
               print(f"oh no, {animal.animal_type}  did not get enough food or care!")                
               print("================ Game Over ================")
               sys.exit()

def run_animal_behaviour(animals,visitors = None):
     for animal in animals:
          print(animal.animal_behaviour(visitors))
          print_separator()
          print()
          time.sleep(2)