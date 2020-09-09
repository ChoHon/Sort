#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define LEN 100000

void insert_max_heap(int h[], int* size, int data) {
	int tmp_size;
	tmp_size = ++(*size);

	while ((tmp_size != 1) && (data > h[tmp_size / 2])) {
		h[tmp_size] = h[tmp_size / 2];
		tmp_size /= 2;
	}

	h[tmp_size] = data;
}

int delete_max_heap(int h[], int* size) {
	int parent, child;
	int root, tmp;

	root = h[1];
	tmp = h[(*size)--];
	parent = 1;
	child = 2;

	while (child <= *size) {
		if ((child < *size) && (h[child] < h[child + 1])) child++;
		if (tmp >= h[child]) break;

		h[parent] = h[child];
		parent = child;
		child *= 2;
	}

	h[parent] = tmp;
	return root;
}

void heap_sort(int list[], int n) {
	int h[LEN + 1];
	int size = 0;

	for (int i = 0; i < n; i++) insert_max_heap(h, &size, list[i]);
	for (int i = (n - 1); i >= 0; i--) list[i] = delete_max_heap(h, &size);

	return;
}

void Check_Sort(int array[], int len) {
	for (int i = 0; i < len - 1; i++) {
		if (array[i] > array[i + 1]) {
			printf("정렬이 잘못되었습니다\n");
			return;
		}
	}
	printf("정렬되어 있습니다.\n");
	return;
}

int main(void) {
	int array[LEN];
	srand(time(NULL));
	for (int i = 0; i < LEN; i++) array[i] = rand() % (LEN + 1);
	clock_t start, end;

	printf("Heap Sort\n");

	printf("Start - ");
	start = clock();
	heap_sort(array, LEN);
	end = clock();
	printf("Finish\n\n");

	printf("정렬 확인\n");
	Check_Sort(array, LEN);
	printf("\n걸린 시간\n%f\n", (double)(end - start) / CLOCKS_PER_SEC);

	return 0;
}