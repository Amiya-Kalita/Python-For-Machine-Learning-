# Binary string (base 2) - starts with '0b'
binary_string = "1010"
decimal_from_binary = int(binary_string, 2)
print(f"The binary string '{binary_string}' is {decimal_from_binary} in decimal.")

# Octal string (base 8) - starts with '0o'
octal_string = "77"
decimal_from_octal = int(octal_string, 8)
print(f"The octal string '{octal_string}' is {decimal_from_octal} in decimal.")

# Hexadecimal string (base 16) - starts with '0x'
hex_string = "FF"
decimal_from_hex = int(hex_string, 16)
print(f"The hexadecimal string '{hex_string}' is {decimal_from_hex} in decimal.")