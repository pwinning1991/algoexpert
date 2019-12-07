def isPalindrome(string):
    reversedString = ''
    for s in string:
        reversedString = s + reversedString
    return string == reversedString

