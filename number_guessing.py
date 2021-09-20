import random

number_easy = random.randint(1, 10)
number_medium = random.randint(1, 50)
number_hard = random.randint(1, 100)
number_tries = 1
active = True

# setting the loop
while active:
    user_mode = input("Pick a mode 'easy, 'medium', or 'hard': ")
    user_mode = user_mode.strip()
    if user_mode in ('easy', 'Easy'):
        user_easy = input("choose a number between 1 and 10: ")
        user_easy = int(float(user_easy))
        while user_easy != number_easy:
            number_tries = number_tries + 1
            # if input is higher than random number print too high
            if 10 >= user_easy > number_easy:
                print("\nYour number is too big")
                user_easy = input("Try again, choose a number between 1 and 10: ")
                user_easy = int(float(user_easy))
            # if input is lower than random number print too low
            elif user_easy < number_easy:
                print("\nYour number is too small")
                user_easy = input("Try again, choose a number between 1 and 10: ")
                user_easy = int(float(user_easy))
            # if input is bigger than 10 print out of range
            elif user_easy > 10:
                print("\nYour number cannot be greater than 10")
                user_easy = input("Try again, choose a number between 1 and 10: ")
                user_easy = int(float(user_easy))
            # if input equal to random number, congrats them, ask if they wanna play again
        if user_easy == number_easy:
            print(f"\nIt took you {number_tries} times to get it right")
            # print out how many tries it took them
            if number_tries >= 3:
                print("You can do better than this")
            else:
                print("Great job so far")
                number_tries = 1
                active = False
                # play again ----
            play_again = input("\nwould you like to play again? y/n: ")
            if play_again in ('y', 'yes', 'Yes'):
                active = True
                number_easy = random.randint(1, 10)
            else:
                    active = False
    # medium mode config ----
    elif user_mode in ('medium', 'Medium'):
        user_medium = input("\nchoose a number between 1 and 50: ")
        user_medium = int(float(user_medium))
        # loop
        while user_medium != number_medium:
            number_tries = number_tries + 1
            # if input is higher than random number print too high
            if 50 >= user_medium > number_medium:
                print("\nYour number is too big")
                user_medium = input("Try again, choose a number between 1 and 50: ")
                user_medium = int(float(user_medium))
            # if input is lower than random number print too low
            elif user_medium < number_medium:
                print("\nYour number is too small")
                user_medium = input("Try again, choose a number between 1 and 50: ")
                user_medium = int(float(user_medium))
            # if input is bigger than 50 print out of range
            elif user_medium > 50:
                print("\nYour number cannot be greater than 50")
                user_medium = input("Try again, choose a number between 1 and 50: ")
                user_medium = int(float(user_medium))
            # if input equal to random number, congrats them, ask if they wanna play again
        if user_medium == number_medium:
            print(f"\nIt took you {number_tries} times to get it right")
            # print out how many tries it took them
            if number_tries >= 5:
                print("You can do better than this")
            else:
                print("Great job so far")
            number_tries = 1
            active = False
            # play again ----
            play_again = input("\nwould you like to play again? y/n: ")
            if play_again in ('y', 'yes', 'Yes'):
                active = True
                number_medium = random.randint(1, 50)
            else:
                active = False
    # hard mode config
    elif user_mode in ('hard', 'Hard'):
        user_hard = input("\nchoose a number between 1 and 100: ")
        user_hard = int(float(user_hard))
        # loop
        while user_hard != number_hard:
            number_tries = number_tries + 1
            # if input is higher than random number print too high
            if 100 >= user_hard > number_hard:
                print("\nYour number is too big")
                user_hard = input("Try again, choose a number between 1 and 100: ")
                user_hard = int(float(user_hard))
            # if input is lower than random number print too low
            elif user_hard < number_hard:
                print("\nYour number is too small")
                user_hard = input("Try again, choose a number between 1 and 100: ")
                user_hard = int(float(user_hard))
            # if input is bigger than 100 print out of range
            elif user_hard > 100:
                print("\nYour number cannot be greater than 100")
                user_hard = input("Try again, choose a number between 1 and 100: ")
                user_hard = int(float(user_hard))
            # if input equal to random number, congrats them, ask if they wanna play again
        if user_hard == number_hard:
            print(f"\nIt took you {number_tries} times to get it right")
            # print out how many tries it took them
            if number_tries >= 15:
                print("You can do better than this")
            else:
                print("Great job so far")
                number_tries = 1
                active = False
            # play again ----
            play_again = input("\nwould you like to play again? y/n: ")
            if play_again in ('y', 'yes', 'Yes'):
                active = True
                number_hard = random.randint(1, 100)
            else:
                active = False
