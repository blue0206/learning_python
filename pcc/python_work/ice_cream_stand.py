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

class IceCreamStand(Restaurant):
    """Represents Ice Cream stand in the Restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla', 'Strawberry', 'Mango', 'Chocolate']
    
    def display_flavors(self):
        print("The following flavors of ice-cream are in stock:")
        for flavor in self.flavors:
            print(f"\t{flavor}")

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

ice_cream_restaurant = IceCreamStand("Blue and Akari's Kitchen", "Ice_Cream")
ice_cream_restaurant.display_flavors()