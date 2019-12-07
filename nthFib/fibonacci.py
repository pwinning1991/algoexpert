def getNthFib(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n -1) + getNthFib(n-2)

# Better space and time complexity because you are recalling the fib(n) mulitple times of the same number
def getNthFib1(n):
    currentAnsewers = {}
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in currentAnsewers.keys():
        return currentAnsewers[n]
    else:
        currentAnsewers[n] =  getNthFib(n -1) + getNthFib(n-2)
        return currentAnsewers[n]




