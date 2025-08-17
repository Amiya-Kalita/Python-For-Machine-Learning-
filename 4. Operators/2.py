my_score = 1500
score_needed_to_level_up = 2000
boss_health = 100

# Do I have the exact score needed to level up? (Probably not!)
print(f"Is my score exactly {score_needed_to_level_up}? {my_score == score_needed_to_level_up}") # Output: False

# Is my score different from what's needed?
print(f"Is my score not equal to {score_needed_to_level_up}? {my_score != score_needed_to_level_up}") # Output: True

# Do I have enough points to level up?
can_level_up = my_score >= score_needed_to_level_up
print(f"Can I level up? {can_level_up}") # Output: False

# Is the boss defeated? (Health is 0 or less)
is_boss_defeated = boss_health <= 0
print(f"Is the boss defeated? {is_boss_defeated}") # Output: False