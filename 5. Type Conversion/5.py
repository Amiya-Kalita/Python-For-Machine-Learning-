my_age = 25
my_pi = 3.14159
is_learning = True
my_list = [1, 2, 3]

# Convert various types to string
age_str = str(my_age)
pi_str = str(my_pi)
learning_str = str(is_learning)
list_str = str(my_list)

print("Age as string:", age_str)          # Output: '25'
print("Pi as string:", pi_str)            # Output: '3.14159'
print("Boolean as string:", learning_str) # Output: 'True'
print("List as string:", list_str)        # Output: '[1, 2, 3]'

# A common use case: combining strings and numbers for output
print("My age is " + str(my_age) + ".")
# An even better way using f-strings (which does the conversion automatically)
print(f"My age is {my_age}.")