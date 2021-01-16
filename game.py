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
def guessing_game():

    name = input("What is your name? >")
    print(f"Welcome {name}")
    random_num = random.randint(0,100)
    print(random_num)
    count = 1

    while True:
        number = int(input("Enter a number between 1 - 100 >"))
        
        if number >= 1 and number <= 100:
            if number != random_num and number < random_num:
                print("Your guess is too low, try again! ")
                count += 1

            elif number != random_num and number > random_num:
                print("Your guess is too high, try again!")
                count += 1

            else:
                print(f"Well done {name}! You found my number in {count} tries!")
                break
        else: 
            print("Sorry, that's not a number between 1 and 100!")

guessing_game()


    
    


