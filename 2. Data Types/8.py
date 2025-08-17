# Creating a set (duplicates are automatically removed)
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits) # Output: {'cherry', 'banana', 'apple'} (order may vary)
print(type(fruits)) # Output: <class 'set'>

# Adding an item
fruits.add("orange")
print("Set after add:", fruits)

# Removing an item
fruits.remove("banana")
print("Set after remove:", fruits)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)          # All unique items from both sets
print("Intersection:", set_a & set_b)   # Items present in both sets