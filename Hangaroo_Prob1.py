secretWord = "engineering"
lettersGuessed = input("Enter a list of letters: ")

def isWordGuessed(secretWord,lettersGuessed):
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True
print (isWordGuessed(secretWord, lettersGuessed))
