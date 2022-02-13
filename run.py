# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import string
from words import words 	# Import words list from words file (https://www.randomlists.com/data/words.json)


def get_word(words):
	word = random.choice(words)
	return word.upper()

def hangman_game():
	word = get_word(words)
	letters = string.ascii_uppercase
	letters_in_word = set(word)
	letters_used = set()
	attempts = 6


	while len(letters_in_word) > 0 and attempts > 0:
		print(attempts, 'attempts left')
		print('You have used: ', ' '.join(letters_used))



		user_input = input('Guess the word: ').upper()
		if user_input in letters_in_word - letters_used:
			letters_used.add(user_input)
			if user_input in letters_in_word:
				letters_in_word.remove(user_input)
				print(' ')

