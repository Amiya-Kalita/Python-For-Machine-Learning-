# Let's set up our inventory
health_potions = 10
coins = 53

# You find 5 more health potions!
total_potions = health_potions + 5
print(f"Total health potions: {total_potions}") # Output: 15

# You use 3 potions
potions_left = total_potions - 3
print(f"Potions left: {potions_left}") # Output: 12

# You find a magic bag that triples your coins!
total_coins = coins * 3
print(f"Wow, I have {total_coins} coins now!") # Output: 159

# You share your coins equally among 4 party members
coins_per_person = total_coins / 4
print(f"Each person gets: {coins_per_person} coins") # Output: 39.75 (Division gives a float)

# Let's see how many coins are left over after sharing
# This is where Floor Division and Modulus are useful!
coins_per_person_whole = total_coins // 4
leftover_coins = total_coins % 4
print(f"Each person gets {coins_per_person_whole} whole coins, and {leftover_coins} are left over.") # Output: 39 whole coins, 3 left over

# You get a power-up! Let's calculate 2 to the power of 3
power_up_strength = 2 ** 3 # This is 2 * 2 * 2
print(f"Power-up strength is: {power_up_strength}") # Output: 8