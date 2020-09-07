import common

unsorted_list = common.makeRandomList()   


def BubbleSort(unsorted):
    length = len(unsorted)
    for i in range(length):
        for j in range(length - i - 1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

    return unsorted


sorted_list = BubbleSort(unsorted_list)

print(sorted_list, common.checkSorted(sorted_list))
