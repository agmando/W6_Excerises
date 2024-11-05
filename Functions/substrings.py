name = input("What is your first and last name? ")

space_index = name.find(' ')

if space_index != -1:
    first_name = name[:space_index]
    last_name = name[space_index + 1:]
else:
    first_name = name
    last_name = ''
    

print(f"Full Name: {name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

