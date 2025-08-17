# Assign the same value to multiple variables
a = b = c = "Hello"
print(a) # Output: Hello
print(b) # Output: Hello
print(c) # Output: Hello

# Assign different values to different variables in one line
x, y, z = 10, 20, 30
print("x is:", x) # Output: x is: 10
print("y is:", y) # Output: y is: 20
print("z is:", z) # Output: z is: 30

# A practical example: swapping variable values
# This is a classic programming problem
tea = "Hot"
coffee = "Cold"

print("Before swap -> Tea:", tea, "Coffee:", coffee)
# Before swap -> Tea: Hot Coffee: Cold

# The Pythonic way to swap them in one line!
tea, coffee = coffee, tea

print("After swap -> Tea:", tea, "Coffee:", coffee)
# After swap -> Tea: Cold Coffee: Hot