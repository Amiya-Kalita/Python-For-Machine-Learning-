# Initialize user_number to a value that fails the condition initially
user_number = 0

# Keep asking while the number is not greater than 10
while user_number <= 10:
    try:
        # Get input from the user
        input_str = input("Please enter a number greater than 10: ")
        # Convert the string input to an integer
        user_number = int(input_str)
        
        # Provide feedback if the number is not valid
        if user_number <= 10:
            print("That's not greater than 10. Try again!")
            
    except ValueError:
        # This runs if the user enters text that is not a number
        print("Invalid input. Please enter a whole number.")

print(f"✅ Success! You entered {user_number}, which is greater than 10.")