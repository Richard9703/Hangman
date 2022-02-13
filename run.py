# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words 	# Import words list from words file (https://www.randomlists.com/data/words.json)


def get_word(words):
	word = random.choice(words)
	return word.upper()



user_guess = True
empty_word = "_" * len(get_word(words))
lives = 0
while user_guess and lives < 5:
	user_input = input("Guess the word: ")
	if user_input == get_word(words):
		word_to_guess = get_word(words).find(user_input)
		empty_word = empty_word[:word_to_guess] + user_guess + empty_word[word_to_guess+1:]
	else:
		lives += 1
		print(f"You have {lives} left")
	print(empty_word)
	if "_" != empty_word:
		print("You are correct!")
		user_guess = False
	if lives == 5:
		print("Try again!")				


get_word(words)


	
