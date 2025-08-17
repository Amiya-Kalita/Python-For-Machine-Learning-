item_name = input("What item are you buying? ")
price = float(input(f"What is the price of one {item_name}? $"))
quantity = int(input(f"How many {item_name}s are you buying? "))

total_cost = price * quantity

# The :.2f inside the f-string formats the number to 2 decimal places for currency
print(f"The total cost for {quantity} {item_name}(s) is ${total_cost:.2f}.")