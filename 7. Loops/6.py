# Search for the number 7 in a list
numbers = [1, 5, 12, 7, 9, 20]

for num in numbers:
    print(f"Checking {num}...")
    if num == 7:
        print("Found the number 7! Stopping the loop.")
        break # Exit the loop now

print("Loop is over.")