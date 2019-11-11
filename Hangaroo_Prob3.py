import string

lettersGuessed = input("Enter a list of letters: ")
def getAvailableLetters(lettersGuessed):
      alphabets = string.ascii_lowercase
      for x in lettersGuessed:
        if x in alphabets:
            alphabets = alphabets.replace(x,"")
      return alphabets
print(getAvailableLetters(lettersGuessed))
