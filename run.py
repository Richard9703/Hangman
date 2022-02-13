# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words

def choose_word(words):
	word = random.randint(0, len(words) -1)
	return words(word)


def hangman(rightWords, wrongWords, hiddenWord):
		

man = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']

# import random
# from words import words 	# Import words list from words file (https://www.randomlists.com/data/words.json)


# def get_word(words):
# 	word = random.choice(words)
# 	return word.upper()



# user_guess = True
# empty_word = "_" * len(get_word(words))
# lives = 0
# while user_guess and lives < 5:
# 	user_input = input("Guess the word: ")
# 	if user_input == get_word(words):
# 		word_to_guess = get_word(words).find(user_input)
# 		empty_word = empty_word[:word_to_guess] + user_guess + empty_word[word_to_guess+1:]
# 	else:
# 		lives += 1
# 		print(f"You have {lives} left")
# 	print(empty_word)
# 	if "_" != empty_word:
# 		print("You are correct!")
# 		user_guess = False
# 	if lives == 5:
# 		print("Try again!")				


# get_word(words)


	
