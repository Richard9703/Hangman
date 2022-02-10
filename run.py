# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import string
from words import words_list # Import words list from words file (https://www.randomlists.com/data/words.json)

def get_random_word(): # chooses a random word from the list
    word = random.choice(words_list)
    while '-'in word or ' ' in word: # Finds a random word even when encountering a ' ' or '-' in the list
        word = random.choice(words_list)

    return word    

