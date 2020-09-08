import common

# 무작위 리스트 생성
unsorted_list = common.makeRandomList()       


def SelectionSort(unsorted):
    length = len(unsorted)
    
    # 역순 전체 반복
    for i in range(length-1, 0, -1):
        # 정렬되어있지 않은 부분에서의 최대값
        idx_max = 0
        
        # 정렬되어있지 않은 부분 반복
        for idx, j in enumerate(unsorted[:i+1]):
            # 최대값 탐색 
            if j > unsorted[idx_max]:
                idx_max = idx
        
        # 최대값 뒤로 이동
        unsorted[idx_max], unsorted[i] = unsorted[i], unsorted[idx_max]

    return unsorted


sorted_list = SelectionSort(unsorted_list)

print(sorted_list, common.checkSorted(sorted_list))