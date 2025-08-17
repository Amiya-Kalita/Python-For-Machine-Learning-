# Creating a tuple
my_tuple = (1, "apple", 3.14, True)
print(my_tuple)
print(type(my_tuple)) # Output: <class 'tuple'>

# Accessing items by index
print("First item:", my_tuple[0]) # Output: 1

# Trying to change an item will cause an error
# my_tuple[0] = "one" # This line would raise a TypeError

# Tuples are useful for fixed data
coordinates = (10.0, 20.5)
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")