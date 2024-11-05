# Define a function to calculate Social Security tax
def get_soc_sec_tax(gross_pay):
    return gross_pay * 0.062  # 6.2% Social Security tax

# Define a function to calculate Medicare tax
def get_medicare_tax(gross_pay):
    return gross_pay * 0.0145  # 1.45% Medicare tax

# Define a function to calculate federal tax based on gross pay and withholding code
def get_federal_tax(gross_pay, withholding_code):
    if withholding_code == 0:
        rate = 0.23  # 23%
    elif withholding_code == 1:
        rate = 0.21  # 21%
    elif withholding_code == 2:
        rate = 0.195  # 19.5%
    elif withholding_code == 3:
        rate = 0.185  # 18.5%
    elif withholding_code >= 4:
        rate = 0.18 - ((withholding_code - 4) * 0.005)  # 18% less 0.5% for each over 4
    return gross_pay * rate

# Sample cases for calculating and displaying taxes
people = [
    {"gross_pay": 750, "withholding_code": 0},
    {"gross_pay": 1550, "withholding_code": 2},
    {"gross_pay": 1100, "withholding_code": 5}
]

# Calculate and display tax details for each person
i = 1

for person in people:
    gross_pay = person["gross_pay"]
    withholding_code = person["withholding_code"]
    soc_sec_tax = get_soc_sec_tax(gross_pay)
    medicare_tax = get_medicare_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay, withholding_code)
    
    print(f"Person {i}:")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Social Security Tax: ${soc_sec_tax:.2f}")
    print(f"Medicare Tax: ${medicare_tax:.2f}")
    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"Withholding Code:{withholding_code }")
    print("--------------------------------------------")
    
    i += 1
