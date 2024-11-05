# Define a global list to store customer data
cust_list = []

class RewardsProgram:

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []  
        self.rewards_points = 0        

    # Method to display the customer's profile
    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    # Method to thank the customer
    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    # Method to add the customer details to the global customer list
    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

    # Method to record a restaurant visit and calculate rewards points
    def visit_rest(self, restaurant_name, food_bill):
        # Add the restaurant to the list of visited restaurants if not already visited
        if restaurant_name not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant_name)

        # Calculate rewards points based on the food bill
        points_for_visit = int(food_bill)  # Convert food bill to points, rounding down
        self.rewards_points += points_for_visit
        
        # Print the rewards information
        print(f"Points for this visit: {points_for_visit}")
        print(f"Total rewards points earned: {self.rewards_points}")
        print(f"Thank you for visiting {restaurant_name}!")

# list with customer and restaurant visit data
customer_data = [
    {"cust_name": "Ronald Mc", "phone": "555-1234", "email": "Rmcdonald@gmail.com", "restaurant_name": "Giordanos", "food_bill": 85.25},
    {"cust_name": "Bobert Perez", "phone": "202-5000", "email": "bob@gmail.com", "restaurant_name": "Sushi Taku", "food_bill": 49.95},
    {"cust_name": "Charlie Brown", "phone": "555-5555", "email": "charliebro@gmail.com", "restaurant_name": "Small Cheval", "food_bill": 24.52}
]

# Process each customer in the combined list
for data in customer_data:
    # Create an instance of RewardsProgram using customer profile data
    customer = RewardsProgram(data["cust_name"], data["phone"], data["email"])
    customer.profile()            
    customer.thank_you()         
    customer.add_to_cust_list()     
    customer.visit_rest(data["restaurant_name"], data["food_bill"]) 
    print(f"Total rewards points: {customer.rewards_points}")
    print("---------------------------------------------------------")

# Display the global cust_list to confirm all customers were added
print("Customer List:")
print(cust_list)



