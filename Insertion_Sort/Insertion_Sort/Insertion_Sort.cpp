#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define LEN 100000

void swap(int* x, int* y) {
	int temp;
	temp = *x; *x = *y; *y = temp;
	return;
}

int Insertion_Sort(int array[], int len) {
	for (int i = 1; i < len; i++) {
		for (int j = i - 1; array[j + 1] < array[j]; j--) swap(&array[j], &array[j + 1]);
	}
	return 0;
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
	srand(time(0));
	for (int i = 0; i < LEN; i++) array[i] = rand() % LEN;
	clock_t start, end;


	printf("Insertion Sort\n");

	printf("Start - ");
	start = clock();
	Insertion_Sort(array, LEN);
	end = clock();
	printf("Finish\n\n");

	printf("정렬 확인\n");
	Check_Sort(array, LEN);
	printf("\n걸린 시간\n%f\n", (double)(end - start) / CLOCKS_PER_SEC);

	return 0;
}