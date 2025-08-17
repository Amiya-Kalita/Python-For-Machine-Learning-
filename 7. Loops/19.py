# A dictionary of products and their inventory count
inventory = {
    "apples": 430,
    "bananas": 312,
    "oranges": 525,
    "pears": 217,
    "cherries": 0
}

# Create a new dictionary for products that are low in stock (less than 300)
low_stock = {}

# Use .items() to get both the product (key) and its count (value)
for product, count in inventory.items():
    if count < 300:
        low_stock[product] = count

print(f"Full inventory: {inventory}")
print(f"Products with low stock: {low_stock}")