#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define LEN 100000

void swap(int* x, int* y) {
	int temp;
	temp = *x; *x = *y; *y = temp;
	return;
}

static int partition(int list[], int left, int right) {
	int pivot = list[left];
	int low = left;
	int high = right + 1;

	do {
		do {
			low++;
		} while (low <= right && list[low] < pivot);

		do {
			high--;
		} while (high >= left && list[high] > pivot);

		if (low < high)
			swap(&list[low], &list[high]);
	} while (low < high);

	swap(&list[left], &list[high]);

	return high;
}

void Quick_Sort(int list[], int left, int right) {
	if (left < right) {
		int q = partition(list, left, right);
		Quick_Sort(list, left, q - 1);
		Quick_Sort(list, q + 1, right);
	}
}

void Check_Sort(int array[], int len) {
	for (int i = 0; i < len - 1; i++) {
		if (array[i] > array[i + 1]) {
			printf("Not Sorted\n");
			return;
		}
	}
	printf("Sorted\n");
	return;
}

int main(void) {
	int array[LEN];
	srand((int)time(NULL));
	for (int i = 0; i < LEN; i++) array[i] = rand() % LEN+1;
	clock_t start, end;
	
	printf("Quick Sort\n");

	printf("Start - ");
	start = clock();
	Quick_Sort(array, 0, LEN - 1);
	end = clock();
	printf("Finish\n\n");

	printf("Check Sort\n");
	Check_Sort(array, LEN);
	printf("\nTime\n%f\n", (double)(end - start) / CLOCKS_PER_SEC);

	return 0;
}