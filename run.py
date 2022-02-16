import random


stages = ['''

  

       +---+

       |   |

           |

           |

           |

           |

     =========''', '''

    

       +---+

       |   |

       O   |

           |

           |

           |

     =========''', '''

    

       +---+

       |   |

       O   |

       |   |

           |

           |

     =========''', '''

    

       +---+

       |   |

       O   |

      /|   |

           |

           |

     =========''', '''

    

       +---+

       |   |

       O   |

      /|\  |

           |

           |

     =========''', '''

    

       +---+

       |   |

       O   |

      /|\  |

      /    |

           |

     =========''', '''

    

       +---+

       |   |

       O   |

      /|\  |

      / \  |

           |

    =========''']

words = ["avocado","chicken","funds","bankrupt","cushion","filming","apartment","radio","detective","vinegar","curtains","carpet","addictive","control","raining","sunshine","diamond","charcoal","chocolate","container","cubes","fan","processor","sunbed","towel","jellyfish", "meals",]


def get_word(word_list):
	word_index = random.randint(0,len(word_list) - 1)
	return word_list[word_index]


def hangman_board(stages, correct_letters, missed_letters, hidden_word):
	print(stages[7 - lives])
	print()

	print("Missed letters:", end="")
	for letter in missed_letters:
		print(letter, end="")
	print()	

	blank = "_" * len(hidden_word)

	for i in range(len(hidden_word)):
		if hidden_word[i] in correct_letters:
			blank = blank[:i] + hidden_word[i] + blank[i+1:]

	for letter in blank:
		print(letter, end="")
	print()	


def get_guess(guessed):
	while True:
		print("Guess a letter: ")
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print("Only one letter at a time")
		elif guess in guessed:
			print("Letter used, use another!")
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print("Enter a letter:")
		else:
			return guess


def try_again(): # Allows the user to play again after finishing the game
   	print("Play again? (yes or no)")
   	return input().lower().startswith("y")


print("HANGMAN")
lives = 7
missed_letters =""
correct_letters = ""
hidden_word = get_word(words)
finished = False

while True:
	hangman_board(stages, correct_letters, missed_letters, hidden_word)

	guess = get_guess(missed_letters + correct_letters) # Type in a letter

	if guess in hidden_word:
		correct_letters = correct_letters + guess

    # checks win
	all_letters = True
	for i in range(len(hidden_word)):
		print("test1")
		if hidden_word[i] not in correct_letters:
			print("test2")
			lives -= 1
			all_letters = False
			break
	if all_letters:
		print("test3")
		print("Hidden word is " + hidden_word + "! You win!")  
		finished = True 
	else:
		print("test4")
		missed_letters = missed_letters + guess   
		

	if len(missed_letters) == len(stages) - 1:
		hangman_board(stages, correct_letters, missed_letters, hidden_word)
		print("No more lives!\n" + str(len(missed_letters)) + "missed letters and " + str(len(correct_letters)) + "correct letters, the word was " + hidden_word + "")
		finsished = True

	
	if finished or lives == 0:
		if try_again():
			missed_letters = ""
			correct_letters = ""
			finish = False 
			hidden_word = get_word(words)
		else:
			break  


