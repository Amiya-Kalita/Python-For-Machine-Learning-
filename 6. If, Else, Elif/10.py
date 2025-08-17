order_total = 115.50

if order_total > 100.00:
    shipping_cost = 0.00
    print("Congratulations! You qualify for FREE shipping.")
elif order_total > 50.00:
    shipping_cost = 5.99
    print(f"Shipping cost is ${shipping_cost}.")
else:
    shipping_cost = 9.99
    print(f"Shipping cost is ${shipping_cost}.")

final_bill = order_total + shipping_cost
print(f"Your final total is: ${final_bill:.2f}")