import common

# 무작위 리스트 생성
unsorted_list = common.makeRandomList()

def Merge(unsorted, left, right):
    # 정렬값 저장을 위한 임시 배열
    temp_list = []

    # 중간값 설정
    mid = (left + right) // 2

    # 정렬을 위한 인덱스 변수
    left_idx, right_idx = left, mid + 1

    # 양쪽 인덱스가 끝에 도달하지 않았을 때 반복문
    while (left_idx <= mid) and (right_idx <= right):
        if unsorted[left_idx] > unsorted[right_idx]:
            temp_list.append(unsorted[right_idx])
            right_idx += 1
        else:
            temp_list.append(unsorted[left_idx])
            left_idx += 1

    # 어느 한쪽 인덱스가 끝에 도달했을 때 다른 한쪽 처리
    if left_idx > mid:
        while right_idx <= right:
            temp_list.append(unsorted[right_idx])
            right_idx += 1
    elif right_idx > right:
        while left_idx <= mid:
            temp_list.append(unsorted[left_idx])
            left_idx += 1

    # 임시 배열에서 본 배열로 이동
    for temp_idx, list_idx in enumerate(range(left, right + 1)):
        unsorted[list_idx] = temp_list[temp_idx]


def MergeSort(unsorted, left, right):
    # 중간값 설정
    mid = (left + right) // 2

    # 재귀 한계 설정
    if left < right:
        
        # 이분
        MergeSort(unsorted, left, mid)
        MergeSort(unsorted, mid + 1, right)

        # 병합
        Merge(unsorted, left, right)


MergeSort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list, common.checkSorted(unsorted_list))


