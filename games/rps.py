import random
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

    print(f'\n\n\tPlayer Score: {player} \tComputer Score: {
          computer} \tDraws: {draw}\n')

    computer_choice = random.randint(1, 3)
    try:
        player_choice = int(
            input("Choose:\n1 for Rock\n2 for Paper\n3 for Scissors\n\n"))
        if 1 <= player_choice <= 3:
            win_conditions = ((1, 3), (2, 1), (3, 2))
            if (player_choice, computer_choice) in win_conditions:
                player += 1
                end_text = "You Win! 🥳"
            elif player_choice == computer_choice:
                draw += 1
                end_text = "Tie Game"
            else:
                computer += 1
                end_text = "Computer Wins! 🤖"
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    print(f'{end_text}')

    keep_playing = input("Press any key to go another round, Q to quit:\n")

    if keep_playing.lower() == "q":
        print(f'\nFinal Score:\tPlayer: {player} \tComputer: {
              computer} \tDraws: {draw}\n')
        break
