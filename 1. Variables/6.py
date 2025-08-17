temp_data = "This is temporary"
print(temp_data) # Output: This is temporary

# Now delete the variable
del temp_data

# The next line will cause a NameError because the variable no longer exists
# print(temp_data)
# NameError: name 'temp_data' is not defined