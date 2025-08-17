# Get temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit using the formula F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Print the conversion, formatting the output to one decimal place
print(f"{celsius}°C is equal to {fahrenheit:.1f}°F.")