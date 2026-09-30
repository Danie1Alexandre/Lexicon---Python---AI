import random
import time

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
            return f"{self.animal_type} feels happy in the sun. Mood increased."

        elif weather in ["Rainy"]:
            return f"{self.animal_type} gets damp and a bit sad. Mood decreased."  
        
        elif weather in ["Snowy"]:
            return f"{self.animal_type} gets cold and a bit sad. Mood decreased."  
      
        elif weather in ["Thunderstorm", "Stormy"]:
            return f"{self.animal_type} takes damage and is scared!"
            
        else:
            return f"{self.animal_type} is doing fine." 
        
    def apply_weather_effect(self,weather):
        if weather in ["Rainy", "Snowy"]:
            self.mood -=1
    
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
                "Energized by the large crowd, the monkeys started clapping their hands and playfully mimicking the visitors!"
            ]
            if self.mood >= 4: 
                print (f"The {self.animal_type} enjoyed the crowd of visitors and started doing acrobatic flips to show off!")
                time.sleep(1)
                reaction = visitors.cheer()
                return reaction
            else:
                return f"The {self.animal_type} {random.choice(special_behaviours)}"
             
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
                animal.mood += 1
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
                animal.mood -= 1
                animal.health -= 1
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
        self.amount = random.randint(19,20)
        return self.amount
    
    def cheer(self):
        return "Visitors are excited and applauding!"


class ZooKeeper(people):
    def __init__(self, role):
        super().__init__(role)

class TroubelMaker(people):
    def __init__(self, role):
        super().__init__(role)



