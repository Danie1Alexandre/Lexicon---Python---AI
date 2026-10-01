import random
import time
from zoo_functions.zoo_functions import print_separator

class Animal:
    def __init__(self, animal_type, health, hunger, mood):
        self.animal_type = animal_type
        self.health = health         
        self.hunger = hunger        
        self.moods = ["Happy", "Neutral", "sad"]
        self.mood = mood # in int

    def feed_animal(self, hp):
        self.health += hp
        self.hunger += 1
        self.mood += 1
    
    def weather_effect(self, weather):
        if weather in ["Sunny", "Clear"]:
            variations = [
                f"{self.animal_type} feels happy in the sun. Mood increased.",
                f"{self.animal_type} is soaking up the sun and stretching out comfortably. Mood increased.",
                f"{self.animal_type} is full of energy thanks to the clear sky! Mood increased."
            ]
            return random.choice(variations)

        elif weather in ["Rainy"]:
            variations = [
                f"{self.animal_type} gets damp and a bit sad. Mood decreased.",
                f"{self.animal_type} is trying to shake off the rainwater and looks grumpy. Mood decreased.",
                f"{self.animal_type} huddles under a shelter to escape the drizzle. Mood decreased."
            ]
            return random.choice(variations)
        
        elif weather in ["Snowy"]:
            variations = [
                f"{self.animal_type} gets cold and a bit sad. Mood decreased.",
                f"{self.animal_type} is shivering from the freezing snow. Mood decreased.",
                f"{self.animal_type} looks blankly at the falling snowflakes. Mood decreased."
            ]
            return random.choice(variations)
    
        elif weather in ["Thunderstorm", "Stormy"]:
            variations = [
                f"{self.animal_type} takes damage and is scared!",
                f"The loud thunder startles {self.animal_type}! Stress causes damage!",
                f"Harsh winds and lightning strike the area! {self.animal_type} loses health!"
            ]
            return random.choice(variations)
            
        else:
            variations = [
                f"{self.animal_type} is doing fine.",
                f"The weather is a bit dull, but {self.animal_type} is relaxed.",
                f"{self.animal_type} is just chilling out in the calm weather."
            ]
            return random.choice(variations)

   
    def apply_weather_effect(self,weather):
        if weather in ["Rainy", "Snowy"]:
            self.mood -=1

        elif weather in ["Sunny", "Clear"]:
            self.mood += 1

        elif weather in ["Thunderstorm", "Stormy"]:
            self.mood -= 1
            self.health -= 1
    
    def animal_behaviour(self, visitors_amount = 0):
        return f" The {self.animal_type} moves around quietly."  
    
    def mood_check(self):
        if self.mood < 1:
            return self.moods[2]

        elif self.mood >= 1 and self.mood < 2:
            return self.moods[1]
        
        else:
            return self.moods[0]
    
    def bad_care_penalty(self):
        if self.mood <= 0:
            self.health -= 1

        if self.hunger <= 0:
            self.health -= 1

    
class Monkey(Animal):
    def __init__(self, animal_type, health, hunger, mood):
        super().__init__(animal_type, health, hunger, mood)
    
    def animal_behaviour(self, visitors = None):
        
        if visitors.amount > 14:
            self.mood +=2
            special_behaviours = [
                "The monkeys got incredibly lively, chattering happily and waving back at the big crowd of visitors!",
                "Energized by the large crowd, the monkeys started clapping their hands and playfully mimicking the visitors!",
                "enjoyed the crowd of visitors and started doing acrobatic flips to show off!"
            ]
            print (f"The {self.animal_type} {random.choice(special_behaviours)}")
            time.sleep(1)
            print_separator()
            print()
            reaction = visitors.cheer()
            return reaction

             
        else:
            behaviours = [
                f"swings between the branches!",
                f"is scratching its head while carefully peeling a hidden banana.",
                f"is making funny faces and pointing at you through the glass!"
            ]

            return f"The {self.animal_type} {random.choice(behaviours)}"

class Lion(Animal):
    def __init__(self, animal_type, health, hunger, mood):
        super().__init__(animal_type, health, hunger, mood)

    def animal_behaviour(self, visitors = None):
        if visitors.amount > 19:
            return f"The {self.animal_type} paces back and forth proudly for the large crowd!"
        else:
            behaviours = [
                "roars loudly!",
                "stretches its heavy paws and takes a lazy nap in the sun.",
                "sharpens its claws against a large wooden log."
            ]
            return f"The {self.animal_type} {random.choice(behaviours)}"

class Dolphin(Animal):
    def __init__(self, animal_type, health, hunger, mood):
        super().__init__(animal_type, health, hunger, mood)
    
    def animal_behaviour(self,visitors = None):
        if visitors.amount > 17:
            return f"The {self.animal_type} does extra high jumps to please the huge crowd!"
        else:
            behaviours = [
                "jumps high in the air and splashes!",
                "swims in fast, elegant circles around the pool.",
                "blows a perfect ring of bubbles through its blowhole!"
            ]
            return f"The {self.animal_type} {random.choice(behaviours)}"
  
    def weather_effect(self, weather):
        if weather in ["Rainy"]:
            return f"{self.animal_type} loves the splashy rain! Mood increased."
        else:
            return super().weather_effect(weather)
    
    def apply_weather_effect(self, weather): # dolpin gets it own effect on rain, Polymorphism 
        if weather in "Rainy":
            self.mood += 1 
        else:
            return super().apply_weather_effect(weather)
    
class Weather:
   
    def __init__(self):

        self.weather_types = [
        "Sunny", "Clear",
        "Rainy", "Snowy", 
        "Thunderstorm", "Stormy",
        "Cloudy", "Foggy",
        ]

    def todays_weather(self): 
        return random.choice(self.weather_types)
    
    def weather_effect(self, weather, animals):
        #weather effects animal class using this method    
        if weather in ["Sunny", "Clear"]:
            for animal in animals:
                animal.apply_weather_effect(weather)            
            return f"☀️  The weather is {weather}."

        elif weather in ["Rainy", "Snowy"]:
            for animal in animals:
                animal.apply_weather_effect(weather)

            if weather == "Snowy":
                return f"❄️  The weather is {weather}."  
            else:                    
                return f"🌧️  The weather is {weather}."  

        elif weather in ["Thunderstorm", "Stormy"]:

            for animal in animals:
                animal.apply_weather_effect(weather)
                
            return f"⚡  EXTREME WEATHER! {weather}."
            
        else:
            return f"☁️  The weather is calm and {weather}." 
   
    
    
#-----------------------------------
class people:
    def __init__(self, role):
        self.name = role
    
class Visitors(people):
    def __init__(self, role, amount):
        self.amount = amount
        super().__init__(role)

    def amount_visitors(self):
        self.amount = random.randint(10,20)
        return self.amount
    
    def cheer(self):
        
        reactions = [
            "Visitors are excited and applauding!",
            "The crowd gasps in awe and dozens of cameras start flashing!",
            "The visitors burst into loud cheers and wave back enthusiastically!"
        ]  
        
        return random.choice(reactions)


# class ZooKeeper(people):
#     def __init__(self, role):
#         super().__init__(role)

# class TroubelMaker(people):
#     def __init__(self, role):
#         super().__init__(role)



