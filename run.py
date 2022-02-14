import random
from words import word_list

"""
Function chooses a random word from the 
imported words list and returns the word 
in uppercase
"""
def pick_random_word():
    word = random.choice(word_list)
    return word.upper()  


"""
User types in their name and 
gets asked if they would like to play Hangman
user is then prompted to enter "y" or "n" to initialize the game. 
"""
def intro_start():
    input_name = input("What is your name?\n")
    print(f"Hello, {input_name}, would you like to play Hangman? y/n")
    answer = None
    while answer not in ("y", "n"):
        answer = input("Enter y or n: ")
        if answer == "y":
            print("Game starting...")
        elif answer == "n":
            print("Closing game..")
        else: 
            print("Please choose an answer...")       


def start_hangman():
    secret_word = "_" * len(word)
    guessed = False
    letters_used = []
    words_used = []
    attempts = 6

def show_lives(attempts):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[attempts]




intro_start()
