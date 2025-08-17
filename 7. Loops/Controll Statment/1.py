numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
  print(f"Checking {num}...")
  if num == 5:
    print("Found the number 5! Breaking the loop.")
    break  # Exit the loop immediately

print("Loop finished.")