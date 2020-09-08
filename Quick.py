import common

# 무작위 리스트 생성
unsorted_list = common.makeRandomList()


def partition(unsorted, left, right):
    pivot = unsorted[left]      # pivot 설정(주어진 리스트 첫번째 값)
    low, high = left + 1, right # 양쪽에서 좁혀오면서 pivot을 중심으로 스위칭할 index

    while True:
        # pivot보다 앞에 위치하지만 큰 값 탐색
        while (low <= right) and (unsorted[low] < pivot):
            low += 1

        # pivot보다 뒤에 위치하지만 작은 값 탐색
        while (high >= left) and (unsorted[high] > pivot):
            high -= 1

        # 위의 두 값을 스위칭
        if low < high:
            unsorted[low], unsorted[high] = unsorted[high], unsorted[low]
            low += 1
            high -= 1
        # low와 high가 교차되었으므로 반복문 종료
        else:
            break

    # pivot를 중심으로 앞에는 작은 값들을, 뒤에는 큰 값들이 위치하게 pivot 위치 조정
    unsorted[left], unsorted[high] = unsorted[high], unsorted[left]

    # pivot 위치 반환
    return high
    

def QuickSort(unsorted, left, right):
    if left < right: # 재귀 한계 설정
        # pivot 중심 분류
        q = partition(unsorted, left, right)

        QuickSort(unsorted, left, q - 1)     # pivot 앞쪽 재귀
        QuickSort(unsorted, q + 1, right)    # pivot 뒷쪽 재귀


QuickSort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list, common.checkSorted(unsorted_list))