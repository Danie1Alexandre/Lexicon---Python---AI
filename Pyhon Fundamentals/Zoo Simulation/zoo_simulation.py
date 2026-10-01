import time
import random
from zoo_class.zoo_class import Animal
from zoo_class.zoo_class import Monkey
from zoo_class.zoo_class import Lion
from zoo_class.zoo_class import Dolphin
from zoo_class.zoo_class import Weather
from zoo_class.zoo_class import Visitors
from zoo_class.zoo_class import TroubelMaker

from zoo_functions.zoo_functions import print_separator
from zoo_functions.zoo_functions import take_user_input
from zoo_functions.zoo_functions import pick_food
from zoo_functions.zoo_functions import end_game_condition
from zoo_functions.zoo_functions import run_animal_behaviour

                   
monkey = Monkey("Monkey \U0001f435", 5, 5, 3)   # \U0001f435 Unicode-code for emoji
lion = Lion("Lion \U0001f981", 5, 5, 1)
dolphin = Dolphin("Dolphin \U0001f42c", 5, 5, 2)
animals =[monkey, lion, dolphin]
visitors = Visitors ("visitors", 10)
troubelMaker = TroubelMaker("TroubelMaker")

# animals2 = [
#     Monkey("Monkey \U0001f435" , "sad", 1),
#     Lion("Lion \U0001f981", "neutral",2),
#     Dolphin("Dolphin \U0001f42c", "Happy", 3)
# ]


food = ["banana", "chicken", "fish"]

zoo_is_alive = 1
weather = Weather()
active_days = 1
day_lenght_sec = 30
day_start_time = time.time()

print_separator()
print("\n================ ZOO SIMULATION ================")
print("use only numbers 1-4 for inputs")
print_separator()
time.sleep(2) # sleep improves game flow by slowing it down

print(f"\n================  DAY {active_days} HAS STARTED ================")
time.sleep(2)
todays_weather = weather.todays_weather() #give the weather of the day

while zoo_is_alive == 1:

    current_time = time.time()
    time_left = current_time - day_start_time #calculate time until new day

    if time_left >= day_lenght_sec:
        active_days += 1
        print(f"\nA new day has dawned! Welcome to DAY {active_days}")
        time.sleep(3)

        for animal in animals:
            animal.health -= 1
            animal.bad_care_penalty()

        end_game_condition(animals)       
        
        day_start_time = time.time()

    todays_weather = weather.todays_weather() 

    print(f"\n================ WEATHER TODAY ================")
    print()
    print(weather.weather_effect(todays_weather, animals), "Day:", active_days)
    
    for animal in animals:
        print(animal.weather_effect(todays_weather))

    print("\n================ MENY ================")
    print("1. Feed animlas")
    print("2. Open the zoo")
    print("3. Watch animals")
    print("4. Close")
    print("\nAnimal Stats")
    
    for animal in animals:
        print(f"{animal.animal_type}  - {animal.mood_check()}, HP {animal.health}  ", end="| ")

    print("\n========================================")

    user_input = take_user_input()

    if user_input == "1":
        print("\n================ Feed animlas ================")
        print("1. Monkey")
        print("2. Lion")
        print("3. Dolphin")
        print("========================================")
        
        user_input = take_user_input()
        
        if user_input == "1":
            pick_food(food)
            user_input = take_user_input()

            if user_input == "1":
                monkey.feed_animal(2)
                print(f"\n{monkey.animal_type} got happy")
                time.sleep(1.5)
     
            elif user_input == "2" or user_input == "3" or user_input == "4":
                print(monkey.animal_type, "got disappointed")
                time.sleep(1.5)            

        elif user_input == "2":
            pick_food(food)
            user_input = take_user_input()           
            
            if user_input == "2":            
                lion.feed_animal(2)
                print(f"\n{lion.animal_type} got happy")
                time.sleep(1.5)
            
            elif user_input == "1" or user_input == "3" or user_input == "4" :
                print(lion.animal_type, "got disappointed")
                time.sleep(1.5)   


        elif user_input == "3":
            pick_food(food)
            user_input = take_user_input()           
            
            if user_input == "3":            
                dolphin.feed_animal(2)
                print(f"\n{dolphin.animal_type} got happy")
                time.sleep(1.5)
            
            elif user_input == "1" or "2" or user_input == "4":    
                print(dolphin.animal_type, "got disappointed")
                time.sleep(1.5)
    
    # open zoo                               
    elif user_input == "2":
        print(f"Zoo open the weather is {todays_weather}")
        time.sleep(1)
        print(f"The zoo have {visitors.amount_visitors()} visitors ")
        time.sleep(3)
        if random.random() < 0.20:
            
            print(troubelMaker.make_loud_noise())
            time.sleep(1)

            for animal in animals:
                animal.mood -= 1
                print_separator
                print(f"{animal.animal_type}'s mood dropped because of the noise.")
                time.sleep(1)

        run_animal_behaviour(animals,visitors)
        time.sleep(1)
        print (visitors.cheer())
        time.sleep(3)

    #watch animals
    elif user_input == "3":
        print("================ Watching Animals ================")
        print()
        run_animal_behaviour(animals,visitors)
        time.sleep(1)
   
    elif user_input == "4":
        print("Good Bye")
        time.sleep(1)     
        break           
   

