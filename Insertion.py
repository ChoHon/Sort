import common

# 무작위 리스트 생성
unsorted_list = common.makeRandomList()


def InsertionSort(unsorted):
    length = len(unsorted)

    # 전체 반복(index 0은 이미 정렬되어있기 때문에 1부터 진행)
    for i in range(1, length):
        # 정렬되어있는 부분을 큰 곳부터 비교하면서 내려옴
        for j in range(i-1, -1, -1):
            # 대소비교 후 스위치
            if unsorted[j + 1] < unsorted[j]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

    return unsorted


sorted_list = InsertionSort(unsorted_list)

print(sorted_list, common.checkSorted(sorted_list))