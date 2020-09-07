import common

unsorted_list = common.makeRandomList()       


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

print(sorted_list, common.checkSorted(sorted_list))