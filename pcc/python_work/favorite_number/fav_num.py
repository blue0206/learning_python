from pathlib import Path

import json


def ask_num(path):
    fav_num = input("Enter your favorite number: ")
    num = json.dumps(fav_num)
    path.write_text(num)

def retrieve_num(path):
    if path.exists():
        num = path.read_text()
        fav_num = json.loads(num)
        return fav_num
    else:
        return None

def greet_num():
    path = Path("num.json")
    fav_num = retrieve_num(path)
    if fav_num:
        print(f"I know your favorite number! It's {fav_num}!")
    else:
        fav_num = ask_num(path)
        print("I'll remember your favorite number!")

greet_num()