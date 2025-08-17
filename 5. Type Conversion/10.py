# Convert characters to their integer codes
char_A = 'A'
char_a = 'a'
char_dollar = '$'

code_A = ord(char_A)
code_a = ord(char_a)
code_dollar = ord(char_dollar)

print(f"The ASCII code for '{char_A}' is {code_A}")
print(f"The ASCII code for '{char_a}' is {code_a}")
print(f"The ASCII code for '{char_dollar}' is {code_dollar}")

# Now, convert the integer codes back to characters
integer_66 = 66
integer_98 = 98

char_from_66 = chr(integer_66)
char_from_98 = chr(integer_98)

print(f"\nThe character for code {integer_66} is '{char_from_66}'")
print(f"The character for code {integer_98} is '{char_from_98}'")