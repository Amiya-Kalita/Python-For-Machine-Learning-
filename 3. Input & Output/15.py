# Get the user's current age and the milestone age
current_age = int(input("What is your current age? "))
milestone_age = int(input("What milestone age are you looking forward to (e.g., 50)? "))

# Calculate the difference
years_to_go = milestone_age - current_age

# Print the result in a full sentence
print(f"You have {years_to_go} years until you turn {milestone_age}.")