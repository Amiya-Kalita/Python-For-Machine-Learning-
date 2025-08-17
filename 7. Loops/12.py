import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
guess_count = 0
guess_limit = 5

print("I'm thinking of a number between 1 and 20.")
print(f"You have {guess_limit} guesses.")

# The loop continues as long as the user has guesses left
while guess_count < guess_limit:
    try:
        guess = int(input("Take a guess: "))
        guess_count += 1 # Use a guess

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 You got it! The number was {secret_number}.")
            break # Exit the loop because the game is won
    except ValueError:
        print("Please enter a valid number.")

# The 'else' block of a loop runs only if 'break' was NOT called
else:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")