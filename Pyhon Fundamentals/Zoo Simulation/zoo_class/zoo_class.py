class Animal:
    def __init__(self, animal_type, mood, health):
        self.animal_type = animal_type
        self. mood = mood 
        self. health = health 

    def feed_animal(self):
        self.health +=1
    
    def weather_effect(self,weather):
        if weather in ["sunny", "clear"]:
            #self.mood += 1
            return f"☀️{self.animal_type} feels happy in the sun. Mood increased."

        elif weather in ["Rainy", "Drizzling"]:
            self.mood -= 1
            return f"🌧️ {self.name} gets damp and a bit sad. Mood decreased."  

        
        elif weather in ["Thunderstorm", "Blizzard", "Stormy"]:
            self.health -= 1
            #self.mood -= 2
            return f"⚡ EXTREME WEATHER! {self.name} takes damage and is scared!"
            
        else:
            return f"☁️ The weather  is calm ({weather}). {self.animal_type} is doing fine."      



weather_types = [
    "Sunny", "Clear", "Cloudy", "Partly cloudy", "Foggy",
    "Rainy", "Drizzling", "Snowy", "Hailing", 
    "Thunderstorm", "Stormy", "Windy"
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

