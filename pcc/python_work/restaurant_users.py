class Restaurant:
    """Tells whether the restaurant is open and what cuisine is served."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type}!")
    
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is currently open!")
    
    def served(self):
        print(f"The restaurant has served {self.number_served} people!")

    def set_number_served(self, num):
        if num > 0:
            self.number_served = num
    
    def increment_number_served(self, num):
        if num > 0:
            self.number_served += num

my_restaurant = Restaurant('Blue\'s Kitchen', 'Dessert')
nino_restaurant = Restaurant('Nino\'s Kitchen', 'Curry')
kayano_restaurant = Restaurant('Akari\'s Kitchen', 'Vegan')

my_restaurant.describe_restaurant()
print("\n")
nino_restaurant.describe_restaurant()
print("\n")
kayano_restaurant.describe_restaurant()
print("\n")

restaurant = Restaurant('Blue and Akari\'s Kitchen', 'Vegan Dessert')
restaurant.open_restaurant
restaurant.describe_restaurant()
restaurant.served()
restaurant.set_number_served(5)
restaurant.served()
restaurant.increment_number_served(8)
restaurant.served()


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

blue = Users("Aayush", "Rai", 16, "Male", "Adventurer Knight/Mage")
rudeus = Users("Rudeus", "Greyrat", 16, "Male", "Mage Knight")
kazuma = Users("Kazuma", "Satou", 16, "Male", "Adventurer")
kayano = Users("Akari", "Yukimura", 16, "Female", "Actress/Adventurer")
sylphie = Users("Sylphiette", "Laws", 16, "Female", "Mage")

print("\n")
blue.greet_user()
blue.describe_user()
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