"""A number-guessing game."""

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player
name = input("What is your name? >")
print(f"Welcome {name}")
number = int(input"Enter a number between 1 - 100 >")