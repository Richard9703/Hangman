import random 

# word list used as words to guess 
word_list = [
    "avocado",
    "chicken",
    "funds",
    "bankrupt",
    "cushion",
    "filming",
    "apartment",
    "radio",
    "detective",
    "vinegar",
    "curtains",
    "carpet",
    "addictive",
    "control",
    "raining",
    "sunshine",
    "diamond",
    "charcoal",
    "chocolate",
    "container",
    "cubes",
    "fan",
    "processor",
    "sunbed",
    "towel",
    "jellyfish",
    "meals",
]

# Takes random word from list and tells you how many letters in the word
word = random.choice(word_list).upper()
print(len(word), "letters long")

# blanks = ['_'] * len(word) # shows the words as '_'
def word_blank():
	word_blank = []
	for i in range(len(word)):
		word_blank.append('_')
	return ''.join(word_blank)	

word_blank = word_blank()
print(word_blank)	

def start(word_blank):
	lives = 0
	word_blank_list = list(word_blank)
	new_word_blank_list = list(word_blank)
	used_letter = list(word_blank)
	used_words = []
	list_words = list(word)

	print("" + ' '.join(word_blank_list))
	while lives < 6:

		user_guess = input("Guess a letter: ")


		if len(user_guess) > 1:
			print("Only 1 letter at a time")
		elif user_guess in used_words:
			print("You already used that letter")	
			print(' '.join(used_words))
		else: 
			used_words.append(user_guess)
			i = 0
			while i < len(word):
				if user_guess == word[i]:
					word_blank[i] = list_words[i]
				i = i+1

			if new_word_blank_list == word_blank_list:
				print("Letter not in word..")
				lives -= 1
				print(lives, "remaining")

				if lives < 6:
					print("Try again!.")
					print(' '.join(word_blank_list))

			elif list_words != word_blank_list:
				
				word_blank_list = new_word_blank_list[:]
				print(' '.join(word_blank_list))

				if list_words == word_blank_list:
					print("You win!\n")
					again = input("Play again? Y/N")
					if again == "Y":
						start()
					quit()
				else:
					print("Try another!")		


def print_scaffold(lives): # prints the scaffold
		if (lives == 0):
				print "_________"
				print "|	 |"
				print "|"
				print "|"
				print "|"
				print "|"
				print "|________"
		elif (lives == 1):
				print "_________"
				print "|	 |"
				print "|	 O"
				print "|"
				print "|"
				print "|"
				print "|________"
		elif (lives == 2):
				print "_________"
				print "|	 |"
				print "|	 O"
				print "|	 |"
				print "|	 |"
				print "|"
				print "|________"
		elif (lives == 3):
				print "_________"
				print "|	 |"
				print "|	 O"
				print "|	\|"
				print "|	 |"
				print "|"
				print "|________"
		elif (lives == 4):
				print "_________"
				print "|	 |"
				print "|	 O"
				print "|	\|/"
				print "|	 |"
				print "|"
				print "|________"
		elif (lives == 5):
				print "_________"
				print "|	 |"
				print "|	 O"
				print "|	\|/"
				print "|	 |"
				print "|	/ "
				print "|________"
		elif (lives == 6):
				print "_________"
				print "|	 |"
				print "|	 O"
				print "|	\|/"
				print "|	 |"
				print "|	/ \ "
				print "|________"
				
				return



print_scaffold(lives)
start(word_blank)
	
