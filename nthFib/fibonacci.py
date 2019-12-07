def getNthFib(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n -1) + getNthFib(n-2)

# Better space and time complexity because you are recalling the fib(n) mulitple times of the same number
def getNthFib1(n, currentAnsewers = {1:0, 2: 1}):
    if n in currentAnsewers.keys():
        return currentAnsewers[n]
    else:
        currentAnsewers[n] =  getNthFib1(n -1, currentAnsewers) + getNthFib1(n-2, currentAnsewers)
        return currentAnsewers[n]


#best time and space 
def getNthFib2(n):
    counter = 3
    init = [0,1]
    while counter <= n:
        next_num = init[0] + init[1]
        init[0], init[1] = init[1], next_num
        counter += 1
    return next_num




