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


# """
# User types in their name and 
# gets asked if they would like to play Hangman
# user is then prompted to enter "y" or "n" to initialize the game. 
# """
# def intro_start():
#     input_name = input("What is your name?\n")
#     print(f"Hello, {input_name}, would you like to play Hangman? y/n")
#     answer = None
#     while answer not in ("y", "n"):
#         answer = input("Enter y or n: ")
#         if answer == "y":
#             print("Game starting...")
           
#         elif answer == "n":
#             print("Closing game..")
#         else: 
#             print("Please choose an answer...")       

"""
Starts the hangman game. 
Users will be prompted to guess the letter or word. 

"""
def start_hangman(word):
    secret_word = "_" * len(word)
    guessed = False
    letters_used = []
    words_used = []
    attempts = 6
    print("\n")
    while not guessed and attempts > 0:
        user_guess = input("Guess the word: ").upper() 
        if user_guess == 1 and user_guess:
            if user_guess in letters_used:
                print("The letter has been used! ", user_guess)
            elif user_guess not in word:
                print(user_guess, "incorrect, try")  
                attempts -= 1
                letters_used.append(user_guess)
            else:
                print("Nice!", user_guess, " is in the word")
                letters_used.append()       
                list_of_words = list(secret_word)
                indices = [i for i, letter in enumerate(word) if letter == user_guess]
                for index in indices:
                    list_of_words[index] = user_guess
                secret_word = "".join(list_of_words)
                if "_" not in secret_word:
                    user_guess = True
        elif len(user_guess) == len(word):
            if user_guess in words_used:
                print(user_guess, " is the answer!")
            elif user_guess != word:
                print(user_guess, " is not the answer...")
                attempts -= 1
                words_used.append(user_guess)
            else:
                guessed = True
                secret_word = word
        else:
            print("Try again...")
        print(show_lives(attempts))
        print(secret_word)
        print("\n")
        if guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            print("The word was " + word + ". Maybe next time!")

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



def main():
    # intro_start()
    word = pick_random_word()
    start_hangman(word)
    while input("Play again? y/n ") == "y":
        word = pick_random_word()
        start_hangman(word)


if __name__ == "__main__":
    main()