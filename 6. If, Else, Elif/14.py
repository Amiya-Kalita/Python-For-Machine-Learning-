print("You stand at a fork in a dark, ancient forest. 🌳")
print("A mossy path leads to the LEFT.")
print("A rickety wooden bridge goes to the RIGHT.")

# Using .lower() makes the input case-insensitive ('LEFT', 'Left', 'left' all work)
choice = input("Which way do you go? (left/right): ").lower()

if choice == "left":
    print("\nYou walk down the mossy path and discover a hidden waterfall.")
    print("Behind the water, you see the faint glimmer of a treasure chest! 💎")
    print("Congratulations, you've found the treasure!")
elif choice == "right":
    print("\nYou cautiously step onto the rickety bridge. It creaks ominously.")
    print("Halfway across, a plank snaps! You fall into the rushing river below.")
    print("GAME OVER. 🌊")
else:
    print("\nConfused, you stand still. The forest grows darker around you.")
    print("You are lost. GAME OVER. 👻")