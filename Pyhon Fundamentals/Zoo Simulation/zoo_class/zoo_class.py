class Animal:
    def __init__(self, animal_type, mood, health):
        self.animal_type = animal_type
        self. mood = mood 
        self. health = health 

    def feed_animal(self):
        self.health +=1
    
    def weather_effect(self,weather):
        if weather == "Sunny" or "Clear":
            return f"{self.animal_type} feels happy in the sun"

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

