import os
import random
from colorama import Fore, init

init(autoreset=True)

attempts = 0
game_active = True
playing = False
lowest = 1
highest = 51
current_guess = 0


def reset_game():
    global attempts, game_active, playing, lowest, highest
    clear_terminal()
    lowest = 1
    highest = 51
    attempts = 0
    game_active = True
    playing = False


def pc_guess():
    clear_terminal()
    guess()
    return print(Fore.MAGENTA + f"Computer Guesses - {current_guess}")


def guess():
    global current_guess
    num_list = list(range(lowest, highest))
    if len(num_list) < 6:
        current_guess = num_list[round(len(num_list) / 2)]
    else:
        current_guess = random.choice(num_list)


def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


while game_active and not playing:
    print(Fore.YELLOW + "\nIn your head, pick a number between 1 and 50. The computer will guess a number, and you, the user, will say whether it is too high, too low, or your number.")
    play_res = input(
        Fore.YELLOW + "\nWhen you have chosen your number, press Enter to play, or Q to quit:\n")
    if play_res.strip().lower() == "q":
        break
    playing = True
    while playing:
        pc_guess()
        user_response = (input(Fore.LIGHTBLUE_EX +
                               "\nEnter one of the following:\nL if number is lower\nH if number is higher\nC if number is correct\n"))
        user_res = user_response.strip().lower()
        print(f"user res: {user_res}")
        if len(user_res) == 1 and user_res in ["l", "h", "c"]:
            attempts += 1
            if user_res == "c":
                print(Fore.GREEN +
                      f"\nComputer guessed correctly in {attempts} attempts!\n")
                playing = False
                game_active = False
            if user_res == "h":
                lowest = current_guess
                pc_guess()
            if user_res == "l":
                highest = current_guess
                pc_guess()
        else:
            print(Fore.RED + "\n*** Input Error ***")
            continue

    if not game_active:
        keep_playing = input(Fore.YELLOW +
                             "Enter any key to play again, Q to quit:\n")

        if keep_playing.strip().lower() == "q":
            print(Fore.MAGENTA + "Thanks for playing!")
            break
        reset_game()
