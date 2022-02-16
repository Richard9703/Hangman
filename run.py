import random
import sys


stages = ['''



       +---+

       |   |

           |

           |

           |

           |

     =========''', '''



       +---+

       |   |

       O   |

           |

           |

           |

     =========''', '''



       +---+

       |   |

       O   |

       |   |

           |

           |

     =========''', '''



       +---+

       |   |

       O   |

      /|   |

           |

           |

     =========''', '''



       +---+

       |   |

       O   |

      /|\  |

           |

           |

     =========''', '''



       +---+

       |   |

       O   |

      /|\  |

      /    |

           |

     =========''', '''



       +---+

       |   |

       O   |

      /|\  |

      / \  |

           |

    =========''']

words = ["avocado", "chicken", "funds", "bankrupt", "cushion", "filming", "apartment", "radio", "detective", "vinegar", "curtains", "carpet", "addictive", "control", "raining", "sunshine", "diamond", "charcoal", "chocolate", "container", "cubes", "fan", "processor", "sunbed", "towel", "jellyfish", "meals"]


def get_word(word_list):
    word_index = random.randint(0, (len(word_list) - 1))
    return word_list[word_index]


def hangman_board(stages, correct_letters, missed_letters, hidden_word):
    print(stages[6 - lives])
    print("You have " + str(lives) + " lives remaining")
    print()

    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    blank = "_" * len(hidden_word)

    for i in range(len(hidden_word)):
        if hidden_word[i] in correct_letters:
            blank = blank[:i] + hidden_word[i] + blank[i+1:]

    for letter in blank:
        print(letter, end=" ")
    print()


def get_guess(guessed):
    while True:
        print("\nGuess a letter: ")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Only one letter at a time")
        elif guess in guessed:
            print("Letter used, use another!")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Enter a letter:")
        else:
            return guess


def try_again():     # Allows the user to play again after finishing the game
        print("Play again? (yes or no)")
        return input().lower().startswith("y")


print("HANGMAN")
lives = 6
missed_letters = ""
correct_letters = ""
hidden_word = get_word(words)
finished = False
while True:
    hangman_board(stages, correct_letters, missed_letters, hidden_word)

    guess = get_guess(missed_letters + correct_letters)     # Type in a letter

    if guess in hidden_word:
        correct_letters = correct_letters + guess

    # checks win
        all_letters = True
        for i in range(len(hidden_word)):
            if hidden_word[i] not in correct_letters:
                all_letters = False
                break
        if all_letters:
            print("Hidden word is " + hidden_word + "! You win!")
            finished = True
    else:
        missed_letters = missed_letters + guess
        lives -= 1

        if lives == 0:
            hangman_board(stages, correct_letters, missed_letters, hidden_word)
            print("No more lives!\n" + str(len(missed_letters)) + " missed letters and " + str(len(correct_letters)) + " correct letters.\nThe word was " + hidden_word + "\n")
            finsished = True
            if try_again():
                missed_letters = ""
                correct_letters = ""
                finished = False
                lives = 6
                hidden_word = get_word(words)
            else:
                sys.exit()
