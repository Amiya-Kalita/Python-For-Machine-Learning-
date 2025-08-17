# Using single quotes
name = 'Alice'
print(name)

# Using double quotes
greeting = "Hello, World!"
print(greeting)
print(type(greeting)) # Output: <class 'str'>

# A multi-line string
long_message = """This is a message
that spans across
multiple lines."""
print(long_message)

# String concatenation (joining strings)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name) # Output: John Doe

# f-Strings (formatted string literals) for easy variable inclusion
age = 30
info = f"{first_name} is {age} years old."
print(info) # Output: John is 30 years old.