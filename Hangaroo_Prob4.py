import string
import random

wordList = ["engineering", "programming", "computer", "calculator", "phone", 
            "ust", "dance", "algebra", "drafting", "tiger"]

def chooseWord(wordList):
    return random.choice(wordList)

secretWord = chooseWord(wordList)

def isWordGuessed(secretWord,lettersGuessed):
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord,lettersGuessed):
       letter_tile = ""
       for x in secretWord:
        if x in lettersGuessed:
            letter_tile += x
        else:
            letter_tile += "_ "
       return letter_tile

def getAvailableLetters(lettersGuessed):
      alphabet = string.ascii_lowercase
      for x in lettersGuessed:
        if x in alphabet:
            alphabet = alphabet.replace(x,"")
      return alphabet
  
def Hangaroo(secretWord):
    length_secretWord = len(secretWord)
    lettersGuessed = []
    guess = str
    numGuess = 5
    wordGuessed = False
    
    print("Hello adventurer! Let's play Hangaroo!")
    print("When you guess the word right, you win! But, if you don't.... Mr.Kangaroo will die!")
    print("I'm thinking of a word that's ", length_secretWord, " letters long.")
    print("Can you guess what it is?")
    
    while numGuess > 0 and numGuess <= 5 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord,lettersGuessed):
            wordGuessed = True
            break
        print ("You have ", numGuess," guesses left adventurer!")
        print ("Available letters: ", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ("Hold on adventurer! You've already guessed that letter: ", getGuessedWord(secretWord,lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ("Amazing guess adventurer!: ", getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Hold on adventurer! You've already guessed that letter: ", getGuessedWord(secretWord,lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                numGuess -= 1
                print ("I'm sorry adventurer! That letter is not in the word: ", getGuessedWord(secretWord,lettersGuessed))
                print ('------------')
    if wordGuessed == True:
        return "Congratulations adventurer, you guessed the word! Mr.Kangaroo gets to live!"
    elif numGuess == 0:
        print ("Ohno! You ran out of guesses. Bye bye Mr.Kangaroo!")
        print ("Better luck next time! The word was ", secretWord, ".")