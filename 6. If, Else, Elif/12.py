weather = "sunny"
temperature_celsius = 28

if weather == "sunny" and temperature_celsius > 25:
    print("It's a hot and sunny day. Perfect for the beach! 🏖️")
elif weather == "sunny" and temperature_celsius <= 25:
    print("It's sunny but not too hot. Great for a walk. 🚶")
elif weather == "rainy":
    print("It's raining. Good day to stay in and watch a movie. 🎬")
elif weather == "snowy":
    print("It's snowing! Let's go build a snowman. ☃️")
else:
    print("Check the weather forecast for more details.")