# Ask for the user's first and last name together
full_name = input("Enter your first and last name: ")

# Split the input string into two variables at the space
first_name, last_name = full_name.split()

# Print the name in a new format
print(f"Your name in reverse is: {last_name}, {first_name}")