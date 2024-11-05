# Define a function to convert Celsius to Fahrenheit
def conv_c_to_f(celsius):
    return round(celsius * 9 / 5 + 32)  # Convert and round to nearest whole number

# Celsius values to be converted
celsius_values = [100, 45, 19, 0, -7, -40]

# Convert and display each Celsius value in Fahrenheit
for c in celsius_values:
    fahrenheit = conv_c_to_f(c)
    print(f"{c}°C is approximately {fahrenheit}°F")
