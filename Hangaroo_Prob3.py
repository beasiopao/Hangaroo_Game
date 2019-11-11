import string

lettersGuessed = input("Enter a list of letters: ")
def getAvailableLetters(lettersGuessed):
      alphabet = string.ascii_lowercase
      for x in lettersGuessed:
        if x in alphabet:
            alphabet = alphabet.replace(x,"")
      return alphabet
print(getAvailableLetters(lettersGuessed))
