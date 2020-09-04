import random

unsorted_list = [random.randrange(1, 500) for x in range(100)]

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
    

def BubbleSort(unsorted):
    length = len(unsorted)
    for i in range(length):
        for j in range(length - i - 1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

    return unsorted

sorted_list = BubbleSort(unsorted_list)
print(sorted_list, checkSorted(sorted_list))
