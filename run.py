# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words 	# Import words list from words file (https://www.randomlists.com/data/words.json)

print("Play Hangman!")
print("You have 6 lives")


# Get words from list
def get_random_word():
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def start():
    word = get_random_word(words)
    num_letters_word = set(word)
    letters = set(string.ascii_uppercase)
    letters_used = set()

    user_letter = input('Guess a letter').upper()
    if user_letter in letter - letters_used:
        letters_used.add(user_letter)
        if user_letter in num_letters_word:
            num_letters_word.remove(user_letter)
    elif user_letter in letters_used:
        print('You have used this letter...Try again.')
    else: 
        print('Invalid character...Try again.')



user_input = input('Types a word: ')
print(user_input)










