# Zoo Simulation

This is an object-oriented Zoo simulation
where you manage a zoo featuring various animals.

## Features
* **Object-Oriented Architecture (OOP):** Uses inheritance and polymorphism for unique animal classes (`Monkey`, `Lion`, `Dolphin`).

* **Dynamic Weather System:** A `Weather` object randomly generates weather conditions that affect the animals' mood and health.

* **Interactive Menu:** Feed animals the correct type of food, open the park, or observe their behavior.

* **Dynamic visitors :** visitors can react on animal behaviors

## Project Structure
* `Zoo Simulation.py` - The main program running the `while` loop and the time system.
* `zoo_class/` - Contains the classes for `Animal`, its subclasses, `people` and `Weather`.

* `zoo_functions/` - Contains helper functions for menus and game-over scenarios.

## How to Run the Program
1. Open your terminal or command prompt in the project folder.
2. Run the following command:
```bash
python zoo_simulation.py
```
3. Use the numbers `1-4` to make selections from the menu.

## Game Rules (Game Over)
If any animal's health drops below 1 due to bad weather or a lack of food, the game ends immediately.