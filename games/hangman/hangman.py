import os
import sys
from colorama import Fore, init
import random
from objects import hangman_words, hangman_stages, welcome_message, game_over_message
init(autoreset=True)

random_word = random.choice(hangman_words)
playing = False
won = False
stage = 0
guessed = ""
answer = ["_" for _ in range(len(random_word))]


def reset_game():
    global guessed, stage, playing, random_word, answer, won
    random_word = random.choice(hangman_words)
    playing = True
    stage = 0
    guessed = ""
    answer = ["_" for _ in range(len(random_word))]
    won = False


def check_guess(str: str):
    global guessed, stage, playing, random_word, won
    clear_terminal()
    if str == "6666":
        return print(Fore.LIGHTCYAN_EX + f"*** {random_word} ***")
    if len(str) != 1:
        return print(Fore.RED + "😅 Input Error: Please enter a letter to continue your quest.")
    match_found = False
    guess = str.lower()
    if guess in guessed:
        return print(Fore.RED + "🔄 Oops! You've already ventured into this territory... 🌀")
    else:
        guessed += guess + " "
    for i, char in enumerate(random_word):
        if char == guess:
            answer[i] = char
            print(Fore.GREEN + "✨ Your keen insight brings you closer to victory!")
            match_found = True
    if not match_found:
        stage += 1
        print(
            Fore.RED + "😔 The shadows grow a little darker. Keep trying, brave adventurer!")
    if "".join(answer) == random_word:
        print(Fore.GREEN +
              f"\n\n\t🏆 Congratulations, intrepid adventurer! 🎉\n\t🌟 You've unraveled the mystery and guessed the word: {random_word}\n\t🥳 Your keen wit and determination have led you to victory!\n")
        won = True


def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


print(Fore.BLACK + welcome_message)
playing_prompt = input(
    Fore.YELLOW + "Press Enter to Let the guessing begin. Q to quit ⏳")
if playing_prompt.lower() == "q":
    sys.exit()
else:
    playing = True
while playing:
    print(Fore.BLUE + f"{hangman_stages[stage]}\n{answer}")
    print(Fore.BLACK + "Guesses: " + guessed)
    player_guess = input(
        Fore.CYAN + "\n🎯 Speak your guess, and let destiny decide:\n")
    check_guess(player_guess.strip())
    if won:
        play_again = input(Fore.YELLOW + "\nEnter to play again, Q to quit:\n")
        if play_again.lower() == "q":
            print(Fore.MAGENTA + "\n Thank you for joining the adventure!\n Your courage and wit made this game a delight.\n Until next time, may your journeys be filled with fun and excitement!\n\n")
            break
        else:
            reset_game()
    if stage == 5:
        print(Fore.MAGENTA + game_over_message)
        print(Fore.MAGENTA + f"📜 The word was: {random_word}")
        play_again = input(
            Fore.YELLOW + "\nWill you rise again to face the shadows? Enter to continue, Q to quit:\n")
        if play_again.lower() == "q":
            print(Fore.MAGENTA + "\n Thank you for joining the adventure!\n Your courage and wit made this game a delight.\n Until next time, may your journeys be filled with fun and excitement!\n\n")
            break
