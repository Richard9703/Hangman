# Hangman 
The Hangman game is a Python project terminal that is deployed the Heroku app.

Users will have to words of various length and use letters to guess the word within 7 lives.

[Live version of my app](https://hangmanproject2022.herokuapp.com/)

![image](https://user-images.githubusercontent.com/91730394/154198087-c878f37d-9f9c-4cac-8ffd-8dd295e5b049.png)


## How to play
[Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses. 

This version is a bit more simplified with a limited number of words to guess from. 

A word will be randomly generated from the list and it will be printed out as blank spaces. 

The player will then be prompted to "Guess a letter" with 7 lives to try and guess the word.

## Features 
- Randomly prints out a word from the list 
- Prints it out as blank 

![image](https://user-images.githubusercontent.com/91730394/154194796-95327dcb-9ab4-4e79-a0f7-9dba53cc1c96.png)

- Accepts user input
- Users are only allowed to enter 1 letter at a time
  - Program checks if you have more than 1 letter in input. It prints out error message informing the user he is only allowed 1 letter per guess.
  - Numbers and symbols are not allowed and will not print out 

![image](https://user-images.githubusercontent.com/91730394/154194880-7dc8351f-c138-44ec-843a-e2efafd3ea39.png)

- Programs checks how many lives you have left depending if you correctly guessed the letter correct or wrong
  - If you guessed correctly it prints out the letter in the blank spaces
  - If you guessed incorrectly it prints out the letter used in the missed letters and takes 1 life away and the program will force you to enter a letter

## Future features
- Add categories of words 
- Add difficulty settings 
   - Easy - 8 lives 
   - Normal - 6 lives
   - Hard - 3 lives

## Testing 
I have tested the program through different application such as:
 - Passed the code through PEP8 Linter
 - Gives correct output when user inputs letters
 - Tested on the Heroku app and 

## Bugs
 ### Solved Bugs
 - No other bugs other than the length of the line of code as mentioned below.
 ### Unsolved Bugs
 - On PEP8 line of code length is too long
 
 ![image](https://user-images.githubusercontent.com/91730394/154196426-539cede9-78c1-4db4-b6a8-b824eb0823a0.png)

# Deployment 
My project was deployed using Code Institute's mock terminal for Heroku
### Steps for deployment
- I cloned the Code Institute repository
- Create a new app on Heroku app 
- Add Python and NodeJS buildbacks 
- Link the Heroku app to the repository
- Click Deploy

# Credits
- Code institute for showing me how to deploy the project
- Wikipedia for the information linked to the Hangman name
