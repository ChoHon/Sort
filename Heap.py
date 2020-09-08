import common

# 최소힙
class MinHeap():
    def __init__(self):        
        self.heap = [-1] # 힙트리(index 1부터 시작하므로 index 0에 trash 값 할당)        
        self.size = 0    # 힙트리 노드 수 겸 마지막 노트 index

    def insert(self, data):
        self.heap.append(data)  # 힙트리 끝에 새로운 data 삽입
        self.size += 1
        new_idx = self.size     # 새로운 data의 index

        # 새로운 data가 힙트리를 올라가는 반복문
        while (new_idx != 1) and (data < self.heap[new_idx // 2]):
            self.heap[new_idx] = self.heap[new_idx // 2]
            new_idx //= 2

        self.heap[new_idx] = data  # 새로운 data 위치 확정


    def delete(self):
        # 마지막 노드 값 저장, root 노드를 마지막 노드로 이동
        last, self.heap[self.size] = self.heap[self.size], self.heap[1] 
        self.size -= 1

        parent = 1
        child = 2

        while child <= self.size:
            # parent와 비교할 child 선택
            if (child < self.size) and (self.heap[child] > self.heap[child + 1]):
                child += 1

            # 힙트리 조정 완료
            if last <= self.heap[child]:
                break

            # 힙트리 조정
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2

        self.heap[parent] = last # 마지막 노드 위치 확정
        return self.heap.pop()


# 무작위 리스트 생성
unsorted_list = common.makeRandomList()


def HeapSort(unsorted):
    minheap = MinHeap()

    # 전부 최소힙에 삽입
    for i in unsorted:
        minheap.insert(i)

    # 힙트리에서 하나씩 빼서 리스트에 저장
    for i in range(len(unsorted)):
        unsorted[i] = minheap.delete()


HeapSort(unsorted_list)
print(unsorted_list, common.checkSorted(unsorted_list))