def print_separator():
     print("_"*40)


def health_check(animal, animal_mood):
     if animal.health < 1:
          animal.mood = animal_mood[2]

     elif animal.health >= 1 and animal.health < 2:
          animal.mood = animal_mood[1]
     
     else:
          animal.mood = animal_mood[0]


def pick_food(food):
     print("\n================ Food ================")
     print("1.", food[0])
     print("2.", food[1])
     print("3.", food[2])
     print("========================================")
