# Print only the odd numbers from 1 to 10
for i in range(1, 11):
    # If the number is even, skip to the next iteration
    if i % 2 == 0:
        continue
    print(i)