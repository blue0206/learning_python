from pathlib import Path

path_cat = Path("cats_and_dogs/cats.txt")
path_dog = Path("cats_and_dogs/dogs.txt")

try:
    contents_cat = path_cat.read_text()
except FileNotFoundError:
    pass
else:
    print(f"{contents_cat}\n")
try:
    contents_dog = path_dog.read_text()
except FileNotFoundError:
    pass
else:
    print(contents_dog)

