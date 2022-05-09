import sys
from random import choice

def play_game():
    print("For exit print 'q'")
    print("Let`s go!")
    digits_string = "0123456789"
    inserting_digit = choice(digits_string[1:11])
    digits_string = digits_string.replace(inserting_digit, "")
    game_string = inserting_digit

    for i in range(0, 3):
        inserting_digit = choice(digits_string)
        digits_string = digits_string.replace(inserting_digit, "")
        game_string += inserting_digit

    step_counter = 1
    user_guess = ""
    while user_guess != game_string:
        user_guess = str(input("Enter your guess"))
        if user_guess == "q":
            sys.exit(0)
        if len(user_guess) != 4:
            print("Please, enter 4 digit!")
            continue
        cows = 0
        bulls = 0
        for i in range(0, 4):
            if game_string[i] == user_guess[i]:
                bulls += 1
            elif user_guess[i] in game_string:
                cows += 1
        if bulls == 4:
            print("You win!")
            print(f"{step_counter}. {user_guess}")
            break
        else:
            print(f"{step_counter}. {user_guess} {bulls} Bulls, {cows} Cows")
            step_counter += 1
    print("Do you want a restart? (y/n)")
    return str(input())

if __name__ == '__main__':
    while True:
        game = play_game()
        if game == 'n' or game == 'q':
            sys.exit(0)


