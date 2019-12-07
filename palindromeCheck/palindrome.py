def isPalindrome(string):
    reversedString = ''
    for s in string:
        reversedString = s + reversedString
    return string == reversedString

def isPalindrome1(string):
    leftidx = 0
    rightidx = len(string) - 1
    while leftidx < rightidx:
        if string[leftidx] != string[rightidx]:
            return False
        leftidx += 1
        rightidx -= 1
    return True

