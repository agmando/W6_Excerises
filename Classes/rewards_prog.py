# Define a global list to store customer data
cust_list = []

class RewardsProgram:

    def __init__(self, cust_name, phone, email):
        # Initialize instance variables for customer name, phone, and email
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

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

# Create instances of the RewardsProgram class for three customers
customers = [
    RewardsProgram("Ronald Mc", "555-1234", "Rmcdonald@gmail.com"),
    RewardsProgram("Bobert Perez", "202-5000", "bob@gmail.com"),
    RewardsProgram("Charlie Brown", "555-5555", "charliebro@gmail.com")
]

# Run methods for each customer
for customer in customers:
    customer.profile()       # Display customer profile
    customer.thank_you()     # Thank the customer
    customer.add_to_cust_list()  # Add customer to global list
    print("---------------------------------------------------------")

# Display the global cust_list to confirm all customers were added
print("Customer List:")
print(cust_list)
