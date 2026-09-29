import time
import random
from zoo_class.zoo_class import Monkey
from zoo_class.zoo_class import Lion
from zoo_class.zoo_class import Dolphin
from zoo_functions.zoo_functions import print_separator
from zoo_functions.zoo_functions import health_check
from zoo_functions.zoo_functions import pick_food



zoo_is_alive = 1

monkey = Monkey("Monkey \U0001f435" , "sad", 1)
lion = Lion("Lion \U0001f981", "neutral",2)
dolphin = Dolphin("Dolphin \U0001f42c", "Happy", 3)

animals =[monkey, lion, dolphin]


animal_mood = ["Happy", "Neutral", "sad"]
food = ["banana", "chicken", "fish"]
active_days = 0

weather_types = [
    "Sunny", "Clear",
    "Rainy", "Snowy", 
    "Thunderstorm", "Stormy"
    "Cloudy", "Foggy",
]


print_separator()
print("\nZOO SIMULATION")
print("use only numbers 1-4 for inputs")
print_separator()



while zoo_is_alive == 1:
    todays_weather = random.choice(weather_types) #the day start at the zoo

    print(f"\n================ WEATHER TODAY: {todays_weather} ================")
    print()
    for animal in animals:
        print(animal.weather_effect(todays_weather))

    print("\n================ MENY ================")
    print("1. Feed animlas")
    print("2. open the zoo")
    print("3. watch animals")
    print("4. close")
    print("\nAnimal Mood")
    for animal in animals:
        print(f"{animal.animal_type}  - {animal.mood} ", end="  | ")
    print("\n========================================")


    user_input = input("pick a number \n")

    if user_input == "1":
        print("\n================ Feed animlas ================")
        print("1. Monkey")
        print("2. Lion")
        print("3. Dolphin")
        print("========================================")
        user_input = input("pick a number \n")
        
        if user_input == "1":
            pick_food(food)
            user_input = input("pick a number")

            if user_input == "1":
                monkey.feed_animal()
                print(f"\n{monkey.animal_type} got happy")
                time.sleep(1.5)
     
            else:
                print(monkey.animal_type, "got disappointed")
     
            monkey.feed_animal()
            health_check(monkey,animal_mood)
               
        elif user_input == "2":
            lion.feed_animal()
            health_check(lion, animal_mood)
                           
   
        elif user_input == "3":
            dolphin.feed_animal()
            health_check(dolphin, animal_mood)
               
        else:
            print("Not a valid option")
            time.sleep(1)

    elif user_input == "2":
        active_days += 1
        
        print("zoo open")
        
        for animal in animals:
            animal.health -= 1
            health_check(animal, animal_mood)
            
            if animal.health < 1:
                print("================ Game Over ================")
                zoo_is_alive = 0
                break
    
    elif user_input == "3":
        print("================ Watching Animals ================")
        print()
        for animal in animals:
            print(animal.animal_behaviour())
   
    elif user_input == "4":
        print("Good Bye")
        time.sleep(1)     
        break           
   

    else:
        print("Not a valid option")
        time.sleep(1)

