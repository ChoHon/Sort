import random

# 무작위 리스트 생성하는 함수
def makeRandomList():
    return [random.randrange(1, 500) for x in range(100)]


# 정렬되었는지 확인하는 함수
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