#include<stdio.h>
int main(void) {
	char arr[10000];
	int count = 0;
	int g = 0;
	fgets(arr, 10000, stdin);
	for (int i = 0; arr[i] != '\0'; i++) {
		count = count + 1;
	}
	for (int i = 0; i < count; i++) {
		if (arr[i] == 'd' && arr[i + 1] == '2') {
			g = g + 1;
			break;
		}
		if (arr[i] == 'D' && arr[i + 1] == '2') {
			g = g + 1;
			break;
		}
	}
	if (g == 1) {
		printf("D2");
	}
	else {
		printf("unrated");
	}
	return 0;
}