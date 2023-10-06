class Users:
    """Greets user and prints their data."""
    def __init__(self, first_name, last_name, age, sex, profession):
        """Initializes user data variables."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.profession = profession
        self.login_attempts = 0
    
    def describe_user(self):
        print("USER INFORMATION:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Profession: {self.profession}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! " +
               "Welcome to the database!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self):
        self.privileges = [
            "Ban Users", 
            "Add Post", 
            "Delete Post", 
            "Mute Users", 
            "Warn Users"
        ]
    
    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(Users):
    def __init__(self, first_name, last_name, age, sex, profession):
        super().__init__(first_name, last_name, age, sex, profession)
        self.privileges = Privileges()
    
    def describe_user(self):
        print("Welcome Administrator Blue!")
        print("ADMINISTRATOR INFORMATION:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Profession: {self.profession}")


blue = Admin("Aayush", "Rai", 16, "Male", "Adventurer Knight/Mage")
rudeus = Users("Rudeus", "Greyrat", 16, "Male", "Mage Knight")
kazuma = Users("Kazuma", "Satou", 16, "Male", "Adventurer")
kayano = Users("Akari", "Yukimura", 16, "Female", "Actress/Adventurer")
sylphie = Users("Sylphiette", "Laws", 16, "Female", "Mage")

print("\n")
blue.describe_user()
blue.privileges.show_privileges()
print("\n")
kayano.greet_user()
kayano.describe_user()
print("\n")
rudeus.greet_user()
rudeus.describe_user()
print("\n")
sylphie.greet_user()
sylphie.describe_user()
print("\n")
kazuma.greet_user()
kazuma.describe_user()

kazuma.increment_login_attempts()
kazuma.increment_login_attempts()
kazuma.increment_login_attempts()
kazuma.increment_login_attempts()
kazuma.increment_login_attempts()
print(f"Kazuma has {kazuma.login_attempts} login attempts!")
kazuma.reset_login_attempts()
print(f"Kazuma's login attempts have been reset to {kazuma.login_attempts}!")