import common

unsorted_list = common.makeRandomList()


def InsertionSort(unsorted):
    length = len(unsorted)

    for i in range(1, length):
        for j in range(i-1, -1, -1):
            if unsorted[j + 1] < unsorted[j]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

    return unsorted


sorted_list = InsertionSort(unsorted_list)

print(sorted_list, common.checkSorted(sorted_list))