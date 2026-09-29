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
    
    def weather_effect(self, weather):
        if weather in ["Sunny", "Clear"]:
            return f"{self.animal_type} feels happy in the sun. Mood increased."

        elif weather in ["Rainy", "snowy"]:
            return f"{self.animal_type} gets damp and a bit sad. Mood decreased."  
      
        elif weather in ["Thunderstorm", "Stormy"]:
            return f"{self.animal_type} takes damage and is scared!"
            
        else:
            return f"{self.animal_type} is doing fine." 

    def animal_behaviour(self):
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
    
    def animal_behaviour(self):
        return f"The {self.animal_type} swings between the branches!" 
     
class Lion(Animal):
    def __init__(self, animal_type, health, hunger, mood):
        super().__init__(animal_type, health, hunger, mood)

    def animal_behaviour(self):
        return f"The {self.animal_type} roars loudly!"
    

class Dolphin(Animal):
    def __init__(self, animal_type, health, hunger, mood):
        super().__init__(animal_type, health, hunger, mood)
    
    def animal_behaviour(self):
        return f"The {self.animal_type} jumps high in the air and splashes!"

class Weather:
   
    def __init__(self):

        self.weather_types = [
        "Sunny", "Clear",
        "Rainy", "Snowy", 
        "Thunderstorm", "Stormy"
        "Cloudy", "Foggy",
        ]

    def todays_weather(self): 
        import random
        return random.choice(self.weather_types)
    
    def weather_effect(self, weather, animals):
        #weather effects animal class using this method    
        if weather in ["Sunny", "Clear"]:
            for animal in animals:
                animal.mood += 1
            return f"☀️  The weather is {weather}"

        elif weather in ["Rainy", "snowy"]:
            for animal in animals:
                animal.mood -= 1
            return f"🌧️  The weather is {weather}"  

        elif weather in ["Thunderstorm", "Stormy"]:

            for animal in animals:
                animal.mood -= 1
                animal.health -= 1
            return f"⚡  EXTREME WEATHER! {weather}"
            
        else:
            return f"☁️  The weather is calm and {weather}" 
   
    
    
#-----------------------------------
# class people:
#     def __init__(self, role):
#         self.name = role

