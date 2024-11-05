# Define a function to convert Fahrenheit to Celsius
def conv_f_to_c(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9)  # Convert and round to nearest whole number

# Fahrenheit values to be converted
fahrenheit_values = [212, 90, 72, 32, 0, -40]

# Convert and display each Fahrenheit value in Celsius
for f in fahrenheit_values:
    celsius = conv_f_to_c(f)
    print(f"{f}°F is approximately {celsius}°C")
