# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import string
from words import words_list # Import words list from words file (https://www.randomlists.com/data/words.json)

def get_random_word(): # chooses a random word from the list
    word = random.choice(words_list)
    return word

def start(word):
	to_complete_word = "_" * len(word)
	guessed = False
	used_letters = []
	used_words = []
	attempt = 6
	print("Start guessing!")
	print(show_aatempts(attempts))
	print(to_complete_word)
	print("\n")
	while not guessed and attempts > 0:
		guess = input("Guess a letter / word: ").upper()
		if len(guess) == 1 and guess.isalpha():

def show_attempts(attempts):
	tries = [
		"""
		Try again x1
		""",
		"""
		Try again x2
		""",
		"""
		Try again x3
		""",
		"""
		Try again x4 
		""",
		"""
		Try again x5 
		""",
		"""
		Try again x6
		""",
	]
	return tries[attempts]






