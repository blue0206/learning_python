from pathlib import Path 

import modules

dog = modules.Dog("Chunchunmaru", 5)
print(f"My dog's name is {dog.name}")
print(f"My dog is {dog.age} years old!")
dog.sit()
dog.roll_over()


path = Path("train/alice.txt")

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file '{path}' does not exist.")
else:
    words = contents.split()
    print(f"The file '{path}' has about {len(words)} words.")    