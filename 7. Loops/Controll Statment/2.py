while True:  # This creates an infinite loop
  user_input = input("Enter a command (or 'quit' to exit): ")
  if user_input.lower() == 'quit':
    break  # Exit the infinite loop
  print(f"Executing command: {user_input}")

print("Program has been terminated.")