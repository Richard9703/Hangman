import sys
import random


input_name = input("What is your name?\n")


# User types in their name
def intro():
    print(f"Hello, {input_name}, would you like to play Hangman?")
    print("Guess the word..")


# Word list
word_list = [
    "avocado",
    "chicken",
    "funds",
    "bankrupt",
    "cushion",
    "filming",
    "apartment",
    "radio",
    "detective",
    "vinegar",
    "curtains",
    "carpet",
    "addictive",
    "control",
    "raining",
    "sunshine",
    "diamond",
    "charcoal",
    "chocolate",
    "container",
    "cubes",
    "fan",
    "processor",
    "sunbed",
    "towel",
    "jellyfish",
    "meals",
]
word = random.choice(word_list)  # Takes random word from word list


attempts = " "
lives = 6
while lives > 0:
    wrong_try = 0
    for char in word:
        if char in attempts:
            print(char)
        else:
            print("_")
            wrong_try = 1

    if wrong_try == 0:
        print("Congratulations!")
        #  Retry the game
        retry = input("Play again? y/n\n")

        if "y" in retry:
            intro()
        elif "n" in retry:
            sys.exit()
        else:
            print("Error")

attempt = input("Guess a letter: ")
attempts = attempt

if attempt not in word:
    lives -= 1
    print("Incorrect!")
    print(f"{lives} remaining!")

if lives == 0:
    print("You lost!")

    retry = input("Play again? y/n\n")

    if "y" in retry:
        intro()
    elif "n" in retry:
        sys.exit()
    else:
        print("Error")


intro()
