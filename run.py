import random

word_list = ["avocado","chicken","funds","bankrupt","cushion","filming","apartment","radio","detective","vinegar","curtains","carpet","addictive","control","raining","sunshine","diamond","charcoal","chocolate","container","cubes","fan","processor","sunbed","towel","jellyfish", "meals",]

def get_word(word_list)
	word = random.choice(word_list)
	return word.upper()



stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
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
   

def hangman_board(stages, correct_letters, wrong_letters, hidden_word):
	print(stages[len(wrong_letters)])
	print()

	print("Wrong letters: ", end="")
	for letter in wrong_letters:
		print(letter, end="")
	print()	

	blank = "_" * len(hidden_word)

	for i in range(len(hidden_word)):
		if hidden_word[i] in correct_letters:
			blank = blank[:i] + hidden_word[i] + blank[i+1:]

	for letter in blank:
		print(letter, end="")
	print()	

	def get_guessed(guessed):
		while True:
			print("Guess a letter: ")
			guess = input()
			guess = guess.lower()
			if len(guess) != 1:
				print("Only one letter at a time")
			elif guess in guessed:
				print("Letter used, use another!")
			elif guess not in 	
