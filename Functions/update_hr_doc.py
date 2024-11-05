# Initial HR list of employee records
hr_list = [
    ('0123', 'HR', 'Rebecca Yang', '69000'),
    ('0121', 'IT', 'Mark Blick', '67000'),
    ('0068', 'IT', 'Kahna Larsen', '112000'),
    ('0234', 'OPS', 'Jim Smith', '54000')
]

# Convert hr_list to a list of lists to make updates easier
hr_list = [list(record) for record in hr_list]

# Update Mark Blick's last name to Blick-Hawley
for record in hr_list:
    if record[2] == 'Mark Blick':  # Check if the name matches Mark Blick
        record[2] = 'Mark Blick-Hawley'  # Update the last name

# Update Jim Smith's department code and salary
for record in hr_list:
    if record[2] == 'Jim Smith':  # Check if the name matches Jim Smith
        record[1] = 'CS'  # Update department code to CS
        record[3] = '60000'  # Update salary to 60000

# Display the updated records in the specified format
print("Employee# | DeptCode | Name         | Salary")
print("--------------------------------------------")
for record in hr_list:
    # Format the salary with commas
    employee_id = record[0]
    dept_code = record[1]
    name = record[2]
    salary = f"{int(record[3]):,}"  # Convert salary to integer and format with commas
    # Display the formatted employee record
    print(f"{employee_id} | {dept_code}      | {name:<17}   | {salary}")