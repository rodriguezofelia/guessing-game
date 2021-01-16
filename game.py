"""A number-guessing game."""
import random
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
count = 1
random_num = random.randint(0,100)
name = input("What is your name? >")
number = int(input("Enter a number between 1 - 100 >"))
print(f"Welcome {name}")

while number >= 1 and number <= 100:
    if number != random_num and number < random_num:
        print("Your guess is too low, try again! ")
        break
        count += 1

    elif number != random_num and number > random_num:
        print("Your guess is too high, try again!")
        break
        count += 1

    else:
        print(f"Well done {name}! You found my number in {count} tries!")
        break


    
    


