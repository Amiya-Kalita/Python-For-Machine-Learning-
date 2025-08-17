my_string = "python"
my_list = ['a', 'b', 'c', 'c']
my_tuple = (1, 2, 3, 1)

# String to list/tuple/set
list_from_str = list(my_string)   # ['p', 'y', 't', 'h', 'o', 'n']
tuple_from_str = tuple(my_string) # ('p', 'y', 't', 'h', 'o', 'n')
set_from_str = set(my_string)     # {'o', 't', 'h', 'n', 'p', 'y'} (order may vary, no duplicates)

print("String to List:", list_from_str)
print("String to Tuple:", tuple_from_str)
print("String to Set:", set_from_str)

# List to tuple/set
tuple_from_list = tuple(my_list) # ('a', 'b', 'c', 'c')
set_from_list = set(my_list)     # {'a', 'c', 'b'} (duplicates removed)

print("\nList to Tuple:", tuple_from_list)
print("List to Set:", set_from_list)