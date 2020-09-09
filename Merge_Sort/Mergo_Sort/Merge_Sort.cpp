#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define LEN 100000

int sorted[LEN];

void swap(int* x, int* y) {
	int temp;
	temp = *x; *x = *y; *y = temp;
	return;
}

void merge(int list[], int left, int mid, int right) {
	int i, j, k, l;
	i = left; j = mid + 1; k = left;

	while (i <= mid && j <= right) {
		if (list[i] < list[j]) {
			sorted[k++] = list[i++];
		}
		else sorted[k++] = list[j++];
	}

	if (i > mid)
		for (l = j; l <= right; l++) sorted[k++] = list[l];
	else
		for (l = i; l <= mid; l++) sorted[k++] = list[l];

	for (l = left; l <= right; l++) list[l] = sorted[l];
}

void Merge_Sort(int list[], int left, int right) {
	int mid;

	if (left < right) {
		mid = (left + right) / 2;
		Merge_Sort(list, left, mid);
		Merge_Sort(list, mid + 1, right);
		merge(list, left, mid, right);
	}
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
	int tmp_array[LEN];
	srand((int)time(NULL));
	for (int i = 0; i < LEN; i++) array[i] = rand() % LEN;
	for (int i = 0; i < LEN; i++) tmp_array[i] = array[i];
	clock_t start, end;

	printf("Merge Sort\n");

	printf("Start - ");
	start = clock();
	Merge_Sort(array, 0, LEN - 1);
	end = clock();
	printf("Finish\n\n");

	printf("정렬 확인\n");
	Check_Sort(array, LEN);
	printf("\n걸린 시간\n%f\n", (double)(end - start) / CLOCKS_PER_SEC);

	return 0;
}