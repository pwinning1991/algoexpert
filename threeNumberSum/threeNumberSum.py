def threeNumberSum(array, targetSum):
    array.sort()
    answer = []
    leftIdx = 1

    for i in range(len(array) - 2):
        leftIdx =  i + 1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            currentSum = array[i] + array[leftIdx] + array[rightIdx]
            if currentSum == targetSum:
                answer.append([array[i],array[leftIdx],array[rightIdx]])
                leftIdx += 1
                rightIdx -= 1
            elif currentSum < targetSum:
                leftIdx += 1
            else:
                rightIdx -= 1
    return answer
