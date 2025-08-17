# In a real program, you'd get input like this:
# choice = input("Do you want to continue? (yes/no/maybe): ")
choice = "maybe"

if choice == "yes":
    print("Great! Let's proceed.")
elif choice == "no":
    print("Okay, stopping the program.")
elif choice == "maybe":
    print("Please make a decision soon!")
else:
    print("Invalid input. Please enter yes, no, or maybe.")