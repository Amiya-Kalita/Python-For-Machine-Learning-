# Search for a number. If it's found, break. If we search the whole list and don't find it, the else block runs.
my_list = [1, 3, 5]
search_for = 4

for item in my_list:
    if item == search_for:
        print(f"Found {search_for}!")
        break
else:
    # This block only runs if the loop finished without a 'break'
    print(f"{search_for} was not found in the list.")