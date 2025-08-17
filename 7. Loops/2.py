# Initialize a variable to hold the user's input
user_input = ""

# Keep looping as long as the user has not typed 'quit'
while user_input.lower() != "quit":
    user_input = input("Enter a message (or type 'quit' to exit): ")
    if user_input.lower() != "quit":
        print(f"You said: {user_input}")

print("Goodbye!")