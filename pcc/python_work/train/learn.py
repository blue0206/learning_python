from pathlib import Path

import modules

dog = modules.Dog("Chunchunmaru", 5)
print(f"My dog's name is {dog.name}")
print(f"My dog is {dog.age} years old!")
dog.sit()
dog.roll_over()

path = Path("train/text.txt")
content = input("Enter Name: ")
path.write_text(content)