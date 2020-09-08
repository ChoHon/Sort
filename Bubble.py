import common

# 무작위 리스트 생성
unsorted_list = common.makeRandomList()   


def BubbleSort(unsorted):
    length = len(unsorted)

    # 전체 반복
    for i in range(length):
        # 정렬되지 않은 부분 반복
        for j in range(length - i - 1):
            # 앞뒤 비교 후 스위칭
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

    return unsorted


sorted_list = BubbleSort(unsorted_list)

print(sorted_list, common.checkSorted(sorted_list))
