student_data = ["Alice", "", "Bob", "Charlie", "", "David"]

for name in student_data:
  if not name: # Checks if the string is empty
    print("Found an empty record. Skipping...")
    continue # Skip this iteration
  
  print(f"Processing data for student: {name}")