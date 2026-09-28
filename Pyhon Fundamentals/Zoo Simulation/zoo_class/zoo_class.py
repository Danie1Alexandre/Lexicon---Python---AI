class Animal:
    def __init__(self, animal_type, mood, health):
        self.animal_type = animal_type
        self. mood = mood 
        self. health = health 

    def feed_animal(self):
        self.health +=1

    
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

