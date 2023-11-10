#include <stdio.h>

int arr[300][300];
int res[10000];

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			scanf("%d", &arr[i][j]);
	}
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int a, b, c, d;
		scanf("%d %d %d %d", &a, &b, &c, &d);

		int cnt = 0;
		for (int q = a - 1; q <= c - 1; q++) {
			for (int p = b - 1; p <= d - 1; p++) {
				cnt += arr[q][p];
			}
		}
		res[i] = cnt;
	}
	for (int i = 0; i < t; i++)
		printf("%d\n", res[i]);
	return 0;
}