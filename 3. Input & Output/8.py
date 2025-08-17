# Get the length and width from the user, converting them to floats
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Perform the calculations
area = length * width
perimeter = 2 * (length + width)

# Print the results using f-strings for clear labeling
print(f"--- Rectangle Dimensions ---")
print(f"Length: {length}")
print(f"Width: {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")