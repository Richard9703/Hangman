# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words_list 	# Import words list from words file (https://www.randomlists.com/data/words.json)

# Start
print("Hangman!")
print("Choose a difficulty:")
print("Normal - 8 lives")
print("Medium - 6 lives")
print("Hard - 3 lives")

choose_difficulty = input("Choose a difficulty! (Type a number to choose)")

def get_random_word():    	# chooses a random word from the list
    word = random.choice(words_list)
    return word









