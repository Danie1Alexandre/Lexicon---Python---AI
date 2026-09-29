import time
from zoo_class.zoo_class import Animal
from zoo_class.zoo_class import Monkey
from zoo_class.zoo_class import Lion
from zoo_class.zoo_class import Dolphin
from zoo_functions.zoo_functions import print_separator

from zoo_functions.zoo_functions import pick_food
from zoo_class.zoo_class import Weather


zoo_is_alive = 1

monkey = Monkey("Monkey \U0001f435", 5, 5, 0)
lion = Lion("Lion \U0001f981", 5, 5, 1)
dolphin = Dolphin("Dolphin \U0001f42c", 5, 5, 2)

animals =[monkey, lion, dolphin]

# animals2 = [
#     Monkey("Monkey \U0001f435" , "sad", 1),
#     Lion("Lion \U0001f981", "neutral",2),
#     Dolphin("Dolphin \U0001f42c", "Happy", 3)
# ]



food = ["banana", "chicken", "fish"]


weather = Weather()
active_days = 0

print_separator()
print("\nZOO SIMULATION")
print("use only numbers 1-4 for inputs")
print_separator()



while zoo_is_alive == 1:
    todays_weather = weather.todays_weather()

    print(f"\n================ WEATHER TODAY ================")
    print()
    print(weather.weather_effect(todays_weather, animals))
    
    for animal in animals:
        print(animal.weather_effect(todays_weather))

    print("\n================ MENY ================")
    print("1. Feed animlas")
    print("2. open the zoo")
    print("3. watch animals")
    print("4. close")
    print("\nAnimal Mood")

    for animal in animals:
        animal.bad_care_penalty()
    
    for animal in animals:
        print(f"{animal.animal_type}  - {animal.mood_check()}, HP {animal.health}  ", end="  | ")


    print("\n========================================")
    print(monkey.mood)
    print(monkey.health)

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
            user_input = input("pick a number \n")

            if user_input == "1":
                monkey.feed_animal(2)
                print(f"\n{monkey.animal_type} got happy")
                time.sleep(1.5)
     
            else:
                print(monkey.animal_type, "got disappointed")
     
        elif user_input == "2":
            lion.feed_animal()
                           
   
        elif user_input == "3":
            dolphin.feed_animal()
               
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
            time.sleep(2)
        time.sleep(2)
   
    elif user_input == "4":
        print("Good Bye")
        time.sleep(1)     
        break           
   

    else:
        print("Not a valid option")
        time.sleep(1)

