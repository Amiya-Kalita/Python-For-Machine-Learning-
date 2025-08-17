is_in_stock = True
account_balance = 50.00
item_price = 35.00

if is_in_stock:
    print("Item is in stock. Proceeding to check balance...")
    # This 'if' is nested inside the first one
    if account_balance >= item_price:
        print(f"Purchase successful! Your new balance is ${account_balance - item_price:.2f}.")
    else:
        print("Purchase failed. Insufficient funds in your account. 😟")
else:
    print("Sorry, this item is currently out of stock.")