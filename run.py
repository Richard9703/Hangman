# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words_list 	# Import words list from words file (https://www.randomlists.com/data/words.json)

print("Play Hangman!")
print("You have 6 lives")


# Get words from list
def get_random_word():
    word = random.choice(words_list).upper()
    return random.choice(word).upper()

letter = get_random_word()

def main():
    num_of_attempts = 0
    guesses = []
    guessed = False
    word_to_guess = '' * len(letter)
    print('Guess the word \"', word_to_guess , '\" It is ', len(word_to_guess))












