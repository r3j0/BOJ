#include <stdio.h>

int main(void) {
	int n, m;
	int arr[100] = { 0, };
	int max = 0;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	for (int i = 0; i < n - 2; i++) {
		for (int j = i+1; j < n - 1; j++) {
			for (int k = j + 1; k < n; k++) {
				if (arr[i] + arr[j] + arr[k] <= m) {
					if (max < arr[i] + arr[j] + arr[k])
						max = arr[i] + arr[j] + arr[k];
				}
			}
		}
	}
	printf("%d",max);
	return 0;
}