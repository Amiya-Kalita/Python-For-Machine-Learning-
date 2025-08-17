age = 22
dress_code_ok = False
is_on_vip_list = True

print("Bouncer is checking your credentials...")

# The parentheses are important here!
# The condition checks for age AND (dress code OR vip status).
if age >= 18 and (dress_code_ok or is_on_vip_list):
    print("Welcome! You can enter the club. ✨")
    # We can add nested 'if' to give a specific reason
    if is_on_vip_list:
        print("(Reason: You are on the VIP list.)")
    else:
        print("(Reason: You meet the age and dress code requirements.)")
elif age < 18:
    print("Access Denied. You are too young. ⛔")
else:
    # This 'else' block catches anyone who is old enough but fails
    # both the dress code and VIP check.
    print("Access Denied. Please check the dress code policy. 👔")