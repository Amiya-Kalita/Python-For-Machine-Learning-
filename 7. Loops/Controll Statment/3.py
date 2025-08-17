for i in range(1, 4):      # Outer loop (runs 3 times for i = 1, 2, 3)
  print(f"Outer loop iteration: i = {i}")
  for j in ['a', 'b', 'c']: # Inner loop
    print(f"  Inner loop iteration: j = {j}")
    if i == 2 and j == 'b':
      print("  BREAKING inner loop!")
      break # This break only affects the inner 'j' loop