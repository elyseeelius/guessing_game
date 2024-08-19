import random
welcome = """
================================
     Number Guessing Game
================================
"""
score_list = []
def start_game():
    attempt_count = 0

    print(welcome)
    random_number = random.randint(1, 10)
    print(random_number)

    while True:
        try:
            guess_number = int(input("Please guess a number from 1 to 10: "))
            if guess_number > 10 or guess_number < 1:
                print("Value must  between 1 and 10")
                continue
        except ValueError:
            print("Please enter a NUMERIC VALUE")
            continue
        attempt_count += 1
        if random_number == guess_number:
            print("Got it!")
            break
        elif random_number < guess_number:
            print("It's lower")
        elif random_number > guess_number:
            print("It's higher")

    print("You have made {} attempts.".format(attempt_count))

    score_list.append(attempt_count)
    print("Your highest score is {}.".format(min(score_list)))

    while True:
        try:
            play_again = input("Want to play again? n/y: ")
        except ValueError:
            print("Enter only Y or N")
            break
        if play_again.lower() == 'y':
            start_game()
        elif play_again.lower() == 'n':
            print("Ok, good bye! See you soon")
        break

start_game()




