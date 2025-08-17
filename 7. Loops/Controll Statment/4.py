numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
  if num % 2 != 0:  # Check if the number is odd
    continue        # If it's odd, skip to the next number
  
  # This line only runs if the 'continue' was not triggered
  print(f"Found an even number: {num}")