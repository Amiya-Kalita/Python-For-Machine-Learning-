price_strings = ["19.99", "25.00", "9.50", "45.75"]

# Convert all strings to floats in one line using a list comprehension
price_floats = [float(price_str) for price_str in price_strings]

# Use the built-in sum() function on the new list of floats
total_price = sum(price_floats)

print(f"Total price (using list comprehension): ${total_price:.2f}")