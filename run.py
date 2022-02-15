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

lives = 6
used_letter = list(word_blank)
used_words = []
list_words = list(word)

while lives > 0:
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

	# user_guess = input("Guess a letter: ").upper()
	# if user_guess in word:
	# 	print("Correct")
	# 	for i,x in enumerate(word):
	# 		if x is user_guess:
	# 			output[i] = user_guess
	# else:
	# 	print("Incorrect", " ", user_guess)			


word_blank()
	
