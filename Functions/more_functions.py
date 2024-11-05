# Define a function to display a mailing label with formatted address details
def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")
    print()  # Blank line for readability

# Define a function to add numbers and display the calculation in a formatted string
def add_numbers(*numbers):
    total = sum(numbers)  # Calculate the total of all numbers
    numbers_str = " + ".join(map(str, numbers))  # Format the numbers for display
    print(f"{numbers_str} = {total}")

# Define a function to display a receipt showing total due, amount paid, and change due
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    if amount_paid >= total_due:
        change_due = amount_paid - total_due
        print(f"Change Due: ${change_due:.2f}")
    else:
        remaining_balance = total_due - amount_paid
        print(f"Remaining Balance: ${remaining_balance:.2f}")
    print()  # Blank line for readability

# Call display_mailing_label() for two different people
display_mailing_label("John Doe", "123 Main St", "Springfield", "IL", "62701")
display_mailing_label("Jane Smith", "456 Oak Ave", "Shelbyville", "TX", "75973")

# Call add_numbers() with varying numbers of arguments
add_numbers(5)
add_numbers(10, 20)
add_numbers(1, 2, 3, 4, 5, 6, 7)

# Call display_receipt() with three scenarios: overpaying, exact payment, and underpaying
display_receipt(100.00, 120.00)  # Overpaid
display_receipt(100.00, 100.00)  # Exact payment
display_receipt(100.00, 80.00)   # Underpaid
