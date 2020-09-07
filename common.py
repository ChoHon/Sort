import random

def makeRandomList():
    return [random.randrange(1, 500) for x in range(100)]

def checkSorted(sorted):
    length = len(sorted)
    isSorted = True
    
    i = 0
    while i < (length - 1):
        if sorted[i] > sorted[i+1]:
            isSorted = False
            break

        i += 1

    return isSorted