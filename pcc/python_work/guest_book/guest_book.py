from pathlib import Path

print("This program creates a guest book.")
print("Enter the names of guest one by one.")
print("Enter 'quit' to stop entering.")

path = Path("./guest_book/guest_book.txt")

guest_names = []
while True:
    name = input("Enter Name: ")
    if name.lower() == 'quit':
        break
    else:
        guest_names.append(name)

guests = ''
for person in guest_names:
    guests += f"{person}\n"

guests = guests.rstrip()
path.write_text(guests)