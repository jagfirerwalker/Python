# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

"""

RULES OF HANGMAN GAME
Here are the requirements for your game:

- The computer must select a word at random from the list of available words that was provided in words.txt. The functions for loading the word list and selecting a random word have already been provided for you in ps3_hangman.py.

The game must be interactive; the flow of the game should go as follows:

- At the start of the game, let the user know how many letters the computer's word contains.

- Ask the user to supply one guess (i.e. letter) per round.

- The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.

- After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.

Some additional rules of the game:
- A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).

- A user loses a guess only when s/he guesses incorrectly.

- If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.

- The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.
"""
import random


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    if set(list(secretWord)) - set(lettersGuessed): #compare if all guessed letters are in secret word
        return False #returns false as not all letters are in secret word
    else:
        return True  #returns true when all letters are being guessed
                

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if set(list(secretWord)) - set(lettersGuessed): #compare if all guessed letters are in secret word
        not_guessed_letters = ([c for c in list(secretWord) if c not in lettersGuessed]) #shows which letters didn't match
        guessedWord = list(secretWord) #create placeholder of word to be guessed
        for item in list(secretWord): #check all letters in secret word
            if item in not_guessed_letters: #if item matches one of the letters that were not guessed replace them with "_"
                guessedWord[guessedWord.index(item)] = "_"
        
        return ' '.join(guessedWord)
    else:
        return ' '.join(([c for c in list(secretWord) if c in lettersGuessed]))
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = list(string.ascii_lowercase)
    return ''.join(sorted(set(list(alphabet)) - set(lettersGuessed)))
      

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses = 8
    letter = []
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    print("-----------")
    
    while not isWordGuessed(secretWord, lettersGuessed):  
            if guesses >= 1:        
                print("You have", guesses, "guesses left")
                print("Available Letters: ",getAvailableLetters(lettersGuessed))
    
                letter = input("Please guess a letter: ")
                letter = letter.lower()
                if letter in lettersGuessed:
                    print("Oops! You've already guessed that letter:", getGuessedWord(secretWord,lettersGuessed))
                    print("-----------")
                else:
                    lettersGuessed.append(letter)
                    if letter in secretWord:
                        print("Good guess:", getGuessedWord(secretWord,lettersGuessed))
                        print("-----------")
                        
                    else:
                        print("Oops! That letter is not in my word:", getGuessedWord(secretWord,lettersGuessed))
                        print("-----------")
                        guesses -= 1   
            else:
                    return print("Sorry, you ran out of guesses. The word was "+str(secretWord) +"." )
            
    else:
            return print("Congratulations, you won!")
        

hangman(chooseWord(wordlist))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
