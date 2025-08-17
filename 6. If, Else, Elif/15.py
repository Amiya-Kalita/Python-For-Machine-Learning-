# In a real app, this would get the current hour automatically.
# Let's set it manually. The current time is around 6 AM in India.
hour_of_day = 6

print(f"The current hour is {hour_of_day}:00.")

if 5 <= hour_of_day < 11:
    suggestion = "a strong Espresso to kickstart your day"
    emoji = "☀️"
elif 11 <= hour_of_day < 16:
    suggestion = "a classic Cappuccino for an afternoon boost"
    emoji = "🌤️"
elif 16 <= hour_of_day < 20:
    suggestion = "a relaxing Decaf to wind down"
    emoji = "🌙"
else:
    suggestion = "something without caffeine, like herbal tea"
    emoji = "😴"

print(f"Good day! How about {suggestion}? {emoji}")