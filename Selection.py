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
        

def SelectionSort(unsorted):
    length = len(unsorted)
    
    for i in range(length-1, 0, -1):
        idx_max = 0
        
        for idx, j in enumerate(unsorted[:i+1]):
            if j > unsorted[idx_max]:
                idx_max = idx
        
        unsorted[idx_max], unsorted[i] = unsorted[i], unsorted[idx_max]

    return unsorted

sorted_list = SelectionSort(unsorted_list)
print(sorted_list, checkSorted(sorted_list))