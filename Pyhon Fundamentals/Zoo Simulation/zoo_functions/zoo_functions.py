def print_separator():
     print("_"*40)


def health_check(animal, animal_mood):
     if animal.health < 1:
          animal.mood = animal_mood[2]

     elif animal.health >= 1 and animal.health < 2:
          animal.mood = animal_mood[1]
     
     else:
          animal.mood = animal_mood[0]
