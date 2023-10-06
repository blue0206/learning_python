from die import Die

sides = input("How many sided dice do you want to roll?\n")
player = Die(sides)
print("Enter 'M' if you want to roll the die multiple times at once.") 
print("Enter 'S' if you want to roll the die just a single time.")
choice = input()
choice = choice.lower()
if choice == 'm':
    player.roll_die_m()
elif choice == 's':
    player.roll_die_s()
else:
    print("You did not enter the roll type.")