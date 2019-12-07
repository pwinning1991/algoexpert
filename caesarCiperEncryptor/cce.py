def cce(string, num):
    newLetters = []
    newKey = num % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)

def getNewLetter(letter, newKey):
    nlc = ord(letter) + newKey
    return chr(nlc) if nlc <= 122 else chr(96 + nlc % 122)
