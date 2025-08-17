# Club rules: You need a VIP pass AND you must be over 18.
has_vip_pass = True
age = 21

# Using 'and'
can_enter_with_and = has_vip_pass and age > 18
print(f"Allowed in based on 'and' rule? {can_enter_with_and}") # Output: True (Both are true)

# Now, let's say another club has a different rule:
# You need a special ticket OR your name must be on the guest list.
has_special_ticket = False
name_on_list = True

# Using 'or'
can_enter_with_or = has_special_ticket or name_on_list
print(f"Allowed in based on 'or' rule? {can_enter_with_or}") # Output: True (One is true)

# Using 'not' to check if someone is NOT a minor.
is_minor = age < 18 # This is False
is_adult = not is_minor # not False -> True
print(f"Is the person an adult? {is_adult}") # Output: True