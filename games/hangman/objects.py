hangman_words = [
    "apple", "banana", "guitar", "computer", "elephant", "bicycle", "airplane",
    "mountain", "dolphin", "python", "kangaroo", "puzzle", "hangman", "umbrella",
    "library", "internet", "sunshine", "chocolate", "penguin", "spaghetti",
    "adventure", "astronaut", "treasure", "squirrel", "microwave", "mushroom",
    "backpack", "fireplace", "caterpillar", "snowflake"
]

welcome_message = """
💀 Welcome, brave soul.... 💀

The gallows await your every misstep.
Guess wisely, for each wrong letter tightens the noose...
The word is your salvation. Can you escape your fate, or will you hang by a thread?
"""

game_over_message = """
💀 Alas, the gallows have claimed another soul... ⚰️

🚫 Your guesses have run dry, and the word remains unclaimed.

📖 Fear not, brave warrior; every end is but a new beginning.
"""

hangman_stages = [
    ' ',
    '''
           -----
           |   |
               |
               |
               |
               |
        =========
        ''',
    '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
    '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
    '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
    '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
]
