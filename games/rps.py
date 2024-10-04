import random
from colorama import Fore, init

init(autoreset=True)

choice_map = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

computer = 0
player = 0
draw = 0

while True:
    end_text = ""

    print(Fore.LIGHTMAGENTA_EX + f'\n\n\tPlayer Score: {player} \tComputer Score: {
          computer} \tDraws: {draw}\n')

    computer_choice = random.randint(1, 3)
    try:
        player_choice = int(
            input(Fore.LIGHTBLUE_EX + "Choose:\n1 for Rock\n2 for Paper\n3 for Scissors\n\n"))
        if 1 <= player_choice <= 3:
            win_conditions = ((1, 3), (2, 1), (3, 2))
            if (player_choice, computer_choice) in win_conditions:
                player += 1
                end_text = Fore.GREEN + "You Win! 🥳"
            elif player_choice == computer_choice:
                draw += 1
                end_text = Fore.LIGHTCYAN_EX + "Tie Game"
            else:
                computer += 1
                end_text = Fore.MAGENTA + "Computer Wins! 🤖"
        else:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 3.")
            continue
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")
        continue

    print(f'\n{end_text}\n')

    keep_playing = input(
        Fore.YELLOW + "Enter any key to go another round, Q to quit:\n")

    if keep_playing.lower() == "q":
        print(Fore.LIGHTMAGENTA_EX + f'\nFinal Score:\tPlayer: {player} \tComputer: {
              computer} \tDraws: {draw}\n')
        print(Fore.LIGHTGREEN_EX + "\t\tThanks for Playing!")
        break
