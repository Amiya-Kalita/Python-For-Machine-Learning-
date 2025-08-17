# Examples of Falsy values
print(f"0 becomes {bool(0)}")           # Output: False
print(f"0.0 becomes {bool(0.0)}")       # Output: False
print(f"'' becomes {bool('')}")         # Output: False
print(f"[] becomes {bool([])}")         # Output: False
print(f"None becomes {bool(None)}")     # Output: False

# Examples of Truthy values
print(f"100 becomes {bool(100)}")         # Output: True
print(f"'Hello' becomes {bool('Hello')}") # Output: True
print(f"[1, 2] becomes {bool([1, 2])}")   # Output: True