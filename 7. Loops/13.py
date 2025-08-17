grades = [88, 92, 100, 75, 83, 95, 61]
total = 0 # Initialize an accumulator variable

# Loop through each grade in the list
for grade in grades:
    total += grade # Add the current grade to the total

# Calculate the average
# The len() function gets the number of items in the list
average = total / len(grades)

print(f"The list of grades is: {grades}")
print(f"The sum of all grades is: {total}")
print(f"The average grade is: {average:.2f}") # .2f formats to 2 decimal places