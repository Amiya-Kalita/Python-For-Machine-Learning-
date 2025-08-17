# Creating a list
my_list = [1, "apple", 3.14, True]
print(my_list)
print(type(my_list)) # Output: <class 'list'>

# Accessing items by index (starts at 0)
print("First item:", my_list[0])  # Output: 1
print("Second item:", my_list[1]) # Output: apple

# Changing an item
my_list[0] = "one"
print("Modified list:", my_list) # Output: ['one', 'apple', 3.14, True]

# Adding an item to the end
my_list.append("new item")
print("List after append:", my_list)

# Removing an item
my_list.remove("apple")
print("List after remove:", my_list)