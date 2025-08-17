# Without parentheses, multiplication happens before addition.
result = 5 + 2 * 3  # Python calculates 2 * 3 first (6), then 5 + 6
print(f"Result without parentheses: {result}")  # Output: 11

# With parentheses, you control the order.
result_with_parens = (5 + 2) * 3  # Python calculates 5 + 2 first (7), then 7 * 3
print(f"Result with parentheses: {result_with_parens}")  # Output: 21