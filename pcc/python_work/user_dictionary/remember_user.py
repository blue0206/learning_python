from pathlib import Path

import json


def verify_user(path, userinfo):
    print("Welcome!") 
    print(f"Is your name {userinfo['First Name']} {userinfo['Last Name']}?")
    verification = input("Enter 'yes' or 'no': ")
    print("\n")
    if verification.lower() == 'yes':
        return True
    else:
        return False

def get_stored_userinfo(path):
    if path.exists():
        contents = path.read_text()
        userinfo = json.loads(contents)
        return userinfo
    else:
        return None

def ask_userinfo(path):
    userinfo = {}
    userinfo['First Name'] = input("Enter your first name: ")
    userinfo['Last Name'] = input("Enter your last name: ")
    userinfo['Age'] = input("Enter Age: ")
    userinfo['Gender'] = input("Enter Gender: ")
    contents = json.dumps(userinfo)
    path.write_text(contents)

def greet_user():
    path = Path("user.json")
    userinfo = get_stored_userinfo(path)
    if userinfo:
        verify = verify_user(path, userinfo)
        if verify:
            welcome = f"Welcome back {userinfo['First Name']} "
            welcome += f"{userinfo['Last Name']}! Here are your details: "
            print(welcome)
            for key, value in userinfo.items():
                print(f"{key}: {value}")
        else:
            userinfo = ask_userinfo(path)
            print("We'll remember your details!")
    else:
        userinfo = ask_userinfo(path)
        print("We'll remember your details!")

greet_user()