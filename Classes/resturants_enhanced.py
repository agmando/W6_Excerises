class Restaurant:

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0  
        self.customer_ratings = []  

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    # Method to add the number of customers served today
    def add_num_served(self):
        customers = int(input("How many customers were served today? "))
        self.number_served += customers

    # Method to print the total number of customers served
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    # Method to add a customer rating
    def customer_rating(self):
        rating = int(input("How would you rate your experience today on a scale of 1-5? "))
        if 1 <= rating <= 5:
            self.customer_ratings.append(rating)
            avg_rating = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for this restaurant is {avg_rating:.2f}.")
        else:
            print("Rating is not in range between 1 and 5.")

# sample cases of the Restaurant class
restaurants = [
    Restaurant("Giordanos", "Pizza"),
    Restaurant("Sushi Taku", "Japanese"),
    Restaurant("Burger King", "Fast food")
]

# Test number served methods

for restaurant in restaurants:
    print("******************************************************")
    restaurant.describe_rest()
    restaurant.print_num_served()  # Initial value
    restaurant.add_num_served()    # Add customers served today
    restaurant.add_num_served()    # Add customers served another time
    restaurant.print_num_served()  # Updated total number served

    # Test customer rating methods
    restaurant.customer_rating()   # Add a customer rating
    restaurant.customer_rating()   # Add another rating
    restaurant.customer_rating()   # Add another rating

    # Test with invalid input for customer_rating
    print("Testing with invalid input:")
    restaurant.customer_rating()   # Try entering an invalid rating
    print("******************************************************")