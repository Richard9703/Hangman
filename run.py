# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words 	# Import words list from words file (https://www.randomlists.com/data/words.json)

print("Play Hangman!")
print("You have 6 lives")


# Get words from words list
get_word = random.choice(words)

# Print letters in '_'
for words in get_word:
    print('_', end=" ")


# Shows the num of letters used
def show_used_letters(used_letters):
	num_letters = 0	
	used_letters = 0
	for char in get_word:
		if char in used_letters:
			print(get_word[num_letters], end=" ")
			used_letters += 1
		else:
			print(" ", end=" ")
		counter += 1
	return used_letters	


# 
def hangman():
	word_length = len(get_word)
	num_wrong_attempts = 0
	guess_index = 0
	letters_guessed = []
	letters_guessed_correct = 0

	while(num_wrong_attempts != 6 and letters_guessed_correct != word_length):
		print("Used letters: ")
		for letter in letters_guessed_correct:
			print(letter, end=" ")
		# User input	
		userInput = input("Guess the word!: ")	
		# User
		if(get_word[guess_index] == userInput):
			print(num_wrong_attempts)
			guess_index += 1
			letters_guessed.append(userInput)
			hangman()
		else:
			num_wrong_attempts += 1
			letters_guessed.append(userInput)
			print(num_wrong_attempts)
			letters_guessed_correct = print(letters_guessed)
			print(hangman)

	print("Nice try!: ")		















def show_hangman(attempts):
	man = [
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

	return man(attempts)







