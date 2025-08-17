username = "admin"
password = "123"

if username == "admin":
    print("Username correct.")
    # This is a nested if statement
    if password == "password123":
        print("Access Granted. Welcome!")
    else:
        print("Incorrect password. Access Denied!")
else:
    print("Incorrect username.")