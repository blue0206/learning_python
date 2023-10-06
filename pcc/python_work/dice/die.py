"""A class that can be used to represent a dice."""

from random import randint

class Die:
    """A class representing a dice."""
    def __init__(self, sides=6):
        """Initializing the attribute."""
        self.sides = sides

    def roll_die_s(self):
        """Rolls the dice and asks whether user wants to roll again."""
        side = int(self.sides)
        print (randint(1, side))
        while True:
            prompt = input("Do you want to roll again? Enter 'Y' if yes: ")
            prompt = prompt.lower()
            if prompt == 'y':
                print(randint(1, side))
            else:
                break
    
    def roll_die_m(self):
        """Rolls the dice a set number of times depending on user input."""
        side = int(self.sides)
        times = input("How many times do you want to roll the dice?\n")
        times = int(times)
        count = 0
        print("Here goes...")
        while count < times:
            print(randint(1, side))
            count += 1