# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

input_name = input("What is your name?\n")

def intro():
	print(f"Hello, {input_name}, would you like to play Hangman?")
	print("Guess the word..")


word_list = ["avocado", "chicken", "funds", "bankrupt", "cushion", "filming", "apartment", "radio", "detective", "vinegar", "curtains", "carpet", "addictive", "control", "raining", "sunshine", "diamond", "charcoal", "chocolate", "container", "cubes", "fan", "processor", "sunbed", "towel", "jellyfish", "meals"]
word = random.choice(word_list)



	
