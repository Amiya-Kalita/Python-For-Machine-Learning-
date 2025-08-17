# 1. Get user input (which is a string)
birth_year_str = input("Enter your year of birth: ")

# 2. Get the current year
current_year = 2025 # Let's assume the current year is 2025

# 3. Explicitly convert the input string to an integer
try:
    birth_year = int(birth_year_str)

    # 4. Perform calculation
    age = current_year - birth_year

    # 5. Print the result (age is an int, but print handles the conversion to string for display)
    print(f"You will be approximately {age} years old in {current_year}.")

except ValueError:
    # 6. Handle cases where the input was not a valid number
    print("Invalid input. Please enter a valid year (e.g., 1995).")