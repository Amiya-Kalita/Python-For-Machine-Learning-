# 1. Initialize a counter variable
count = 1

# 2. Set the condition
while count <= 5:
    print(f"The current count is: {count}")
    # 3. IMPORTANT: Update the counter. Without this, it's an infinite loop!
    count = count + 1 # or count += 1

print("Loop finished!")