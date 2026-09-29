class Animal:
    def __init__(self, animal_type, mood, health):
        self.animal_type = animal_type
        self. mood = mood 
        self. health = health 

    def feed_animal(self):
        self.health +=1
    
    def weather_effect(self, weather):
        
        if weather in ["Sunny", "Clear"]:
            #self.mood += 1
            return f"☀️  The weather is {weather}, the {self.animal_type} feels happy in the sun. Mood increased."

        elif weather in ["Rainy", "Drizzling"]:
            #self.mood -= 1
            return f"🌧️  The weather is {weather},  the {self.animal_type} gets damp and a bit sad. Mood decreased."  

        
        elif weather in ["Thunderstorm", "Blizzard", "Stormy"]:
            self.health -= 1
            #self.mood -= 2
            return f"⚡  EXTREME WEATHER! the {self.animal_type} takes damage and is scared!"
            
        else:
            return f"☁️  The weather  is calm and {weather}. the {self.animal_type} is doing fine."      



weather_types = [
    "Sunny", "Clear",
    "Rainy", "Snowy", 
    "Thunderstorm", "Stormy"
    "Cloudy", "Foggy",
]


    
class Monkey(Animal):
    def __init__(self, animal_type, mood, health ):
        super().__init__(animal_type,mood, health )
     
class Lion(Animal):
    def __init__(self, animal_type, mood, health ):
        super().__init__(animal_type,mood, health )

class Dolphin(Animal):
    def __init__(self, animal_type, mood, health ):
        super().__init__(animal_type,mood, health )

        
#-----------------------------------
# class people:
#     def __init__(self, role):
#         self.name = role

