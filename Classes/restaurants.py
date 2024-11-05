# Define the Restaurant class
class Restaurant:
    """
    A class to represent a restaurant.
    Stores the restaurant's name and the type of food it serves.
    """

    def __init__(self, rest_name, food_type):
        # Initialize instance variables for the restaurant's name and food type
        self.rest_name = rest_name
        self.food_type = food_type

    # Method to describe the restaurant
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    # Method to indicate the restaurant is open
    def rest_open(self):
        print(f"{self.rest_name} is open.")

# Create instances of the Restaurant class
restaurant1 = Restaurant("Giordanos", "Pizza")
restaurant2 = Restaurant("Mcdonalds", "Fast Food")
restaurant3 = Restaurant("Small Cheval", "Burgers")

# Call describe_rest() and rest_open() for each instance
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()
