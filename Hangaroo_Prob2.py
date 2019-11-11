secretWord = "engineering"
lettersGuessed = input("Enter a list of letters: ")

def getGuessedWord(secretWord,lettersGuessed):
       letter_tile = ""
       for x in secretWord:
        if x in lettersGuessed:
            letter_tile += x
        else:
            letter_tile += "_ "
       return letter_tile
print(getGuessedWord(secretWord,lettersGuessed))
