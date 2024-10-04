import random
from colorama import Fore, init

init(autoreset=True)

attempts = 0
game_active = True
answer = random.randint(1, 9)


def reset_game():
    global attempts, answer, game_active
    attempts = 0
    answer = random.randint(1, 9)
    game_active = True


while game_active:
    try:
        guess = int(input(Fore.LIGHTBLUE_EX +
                    "\n*** Pick a number 1 - 9 ***\n"))
        if 1 <= guess <= 9:
            attempts += 1
            if guess == answer:
                print(Fore.GREEN +
                      f"\nYou guessed correctly in {attempts} attempts!\n")
                game_active = False
            elif guess < answer:
                print(Fore.RED + "Too Low!")
            elif guess > answer:
                print(Fore.RED + "Too High!")
        else:
            print("Invalid input. Please enter a number between 1 and 9")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if not game_active:
        keep_playing = input(Fore.YELLOW +
                             "Enter any key to play again, Q to quit:\n")

        if keep_playing.lower() == "q":
            print(Fore.MAGENTA + "Thanks for playing!")
            break
        reset_game()
