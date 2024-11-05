# Define a function to extract the supplier code from the part code
def get_supplier_code(part_code):
    # Split the part code at ':' and return the first part as supplier code
    return part_code.split(":")[0]

# Define a function to extract the product number from the part code
def get_product_num(part_code):
    # Split the part code at ':' and then at '-', and return the product code part
    return part_code.split(":")[1].split("-")[0]

# Define a function to extract the size from the part code
def get_size(part_code):
    # Split the part code at '-' and return the second part as size
    return part_code.split("-")[1]

# Create variables to hold the example part codes
part_code_1 = "ACME:123-L"
part_code_2 = "DI:12345-M"
part_code_3 = "ACE:1-12"

# Process and display results for each part code
for part_code in [part_code_1, part_code_2, part_code_3]:
    # Extract supplier, product number, and size
    supplier = get_supplier_code(part_code)
    product_num = get_product_num(part_code)
    size = get_size(part_code)
    
    # Display the extracted information
    print(f"Part #{product_num}, size {size}, supplied by {supplier}")
