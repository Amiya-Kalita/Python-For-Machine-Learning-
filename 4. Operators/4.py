# Player and Enemy stats
my_mana = 75
my_level = 12
is_enemy_asleep = False

# Let's check the conditions using operators!
# 1. Comparison Operator: Check mana
has_enough_mana = my_mana > 50 # This will be True (75 > 50)

# 2. Logical Operator: Check if enemy is NOT asleep
enemy_is_awake = not is_enemy_asleep # not False -> This will be True

# 3. Comparison Operator: Check level
is_high_enough_level = my_level >= 10 # This will be True (12 >= 10)

# 4. Logical Operator: Combine all conditions with 'and'
can_do_special_attack = has_enough_mana and enemy_is_awake and is_high_enough_level

# The final decision!
print(f"Can I perform the special attack? {can_do_special_attack}") # Output: True