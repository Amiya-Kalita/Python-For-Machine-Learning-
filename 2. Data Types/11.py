# A variable with no value assigned yet
winner = None
print(winner)
print(type(winner)) # Output: <class 'NoneType'>

if winner is None:
    print("The game is not over yet.")