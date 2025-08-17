username = ""
password = "123"

# Using 'or' to check if either condition is bad
if len(username) == 0 or len(password) < 8:
    print("Validation Error: ❌")
    # Nested 'if' to give specific feedback
    if len(username) == 0:
        print("- Username cannot be empty.")
    if len(password) < 8:
        print("- Password must be at least 8 characters long.")
else:
    print("Registration successful! 👍")