# Creating a dictionary
person = {
    "name": "Bob",
    "age": 25,
    "city": "New York"
}
print(person)
print(type(person)) # Output: <class 'dict'>

# Accessing a value by its key
print("Name:", person["name"]) # Output: Bob

# Changing a value
person["age"] = 26
print("Updated dictionary:", person)

# Adding a new key-value pair
person["job"] = "Engineer"
print("Final dictionary:", person)

# Getting all keys or values
print("Keys:", person.keys())
print("Values:", person.values())