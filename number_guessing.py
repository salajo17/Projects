import random

number_easy = random.randint(1, 10)
number_medium = random.randint(1, 50)
number_hard = random.randint(1, 100)
number_tries = 1
active = True

while active:
    user_mode = input("Pick a mode 'easy, 'medium', or 'hard': ")
    if user_mode in ('easy', 'Easy'):
        user_easy = input("choose a number between 1 and 10: ")
        user_easy = int(float(user_easy))
        while user_easy != number_easy:
            number_tries = number_tries + 1
            if 10 >= user_easy > number_easy:
                print("\nYour number is too big")
                user_easy = input("Try again, choose a number between 1 and 10: ")
                user_easy = int(float(user_easy))
                ###
            elif user_easy < number_easy:
                print("\nYour number is too small")
                user_easy = input("Try again, choose a number between 1 and 10: ")
                user_easy = int(float(user_easy))
                ###
            elif user_easy > 10:
                print("\nYour number cannot be greater than 10")
                user_easy = input("Try again, choose a number between 1 and 10: ")
                user_easy = int(float(user_easy))
                ###
            if user_easy == number_easy:
                print(f"\nIt took you {number_tries} times to get it right")
                ###
                if number_tries >= 4:
                    print("You can do better than this")
                else:
                    print("Great job so far")
                number_tries = 1
                active = False
                # play again ----
                play_again = input("\nwould you like to play again? y/n: ")
                if play_again in ('y', 'yes', 'Yes'):
                    active = True
                else:
                    active = False
    # medium mode config ----
    elif user_mode in ('medium', 'Medium'):
        user_medium = input("\nchoose a number between 1 and 50: ")
        user_medium = int(float(user_medium))
        while user_medium != number_medium:
            number_tries = number_tries + 1
            if 50 >= user_medium > number_medium:
                print("\nYour number is too big")
                user_medium = input("Try again, choose a number between 1 and 50: ")
                user_medium = int(float(user_medium))
                ###
            elif user_medium < number_medium:
                print("\nYour number is too small")
                user_medium = input("Try again, choose a number between 1 and 50: ")
                user_medium = int(float(user_medium))
                ###
            elif user_medium > 50:
                print("\nYour number cannot be greater than 50")
                user_medium = input("Try again, choose a number between 1 and 50: ")
                user_medium = int(float(user_medium))
                ###
            if user_medium == number_medium:
                print(f"\nIt took you {number_tries} times to get it right")
                if number_tries >= 10:
                    print("You can do better than this")
                else:
                    print("Great job so far")
                number_tries = 1
                active = False
                # play again ----
                play_again = input("\nwould you like to play again? y/n: ")
                if play_again in ('y', 'yes', 'Yes'):
                    active = True
                else:
                    active = False
    # hard mode config
    elif user_mode in ('hard', 'Hard'):
        user_hard = input("\nchoose a number between 1 and 100: ")
        user_hard = int(float(user_hard))
        while user_hard != number_hard:
            number_tries = number_tries + 1
            if 100 >= user_hard > number_hard:
                print("\nYour number is too big")
                user_hard = input("Try again, choose a number between 1 and 100: ")
                user_hard = int(float(user_hard))
                ###
            elif user_hard < number_hard:
                print("\nYour number is too small")
                user_hard = input("Try again, choose a number between 1 and 100: ")
                user_hard = int(float(user_hard))
                ###
            elif user_hard > 100:
                print("\nYour number cannot be greater than 100")
                user_hard = input("Try again, choose a number between 1 and 100: ")
                user_hard = int(float(user_hard))
                ###
            if user_hard == number_hard:
                print(f"\nIt took you {number_tries} times to get it right")
                if number_tries >= 25:
                    print("You can do better than this")
                else:
                    print("Great job so far")
                number_tries = 1
                active = False
                # play again ----
                play_again = input("\nwould you like to play again? y/n: ")
                if play_again in ('y', 'yes', 'Yes'):
                    active = True
                else:
                    active = False
