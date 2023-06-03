#include <stdio.h>

int arr[1000][1000] = { 0, };
int queue[1000000][2] = { 0, };
int queue_size = 0;
int count = 0;
int m, n;

void search(int sero, int garo, int next_day, int now_count) {
	if (garo > 0) {
		if (arr[sero][garo - 1] == 0) {
			arr[sero][garo - 1] = 1;
			queue[queue_size][0] = sero;
			queue[queue_size++][1] = garo - 1;
		}
	}
	if (garo < m - 1) {
		if (arr[sero][garo + 1] == 0) {
			arr[sero][garo + 1] = 1;
			queue[queue_size][0] = sero;
			queue[queue_size++][1] = garo + 1;
		}
	}
	if (sero > 0) {
		if (arr[sero - 1][garo] == 0) {
			arr[sero - 1][garo] = 1;
			queue[queue_size][0] = sero - 1;
			queue[queue_size++][1] = garo;
		}
	}
	if (sero < n - 1) {
		if (arr[sero + 1][garo] == 0) {
			arr[sero + 1][garo] = 1;
			queue[queue_size][0] = sero + 1;
			queue[queue_size++][1] = garo;
		}
	}

	if (now_count == next_day - 1) {
		if (next_day != queue_size) {
			next_day = queue_size;
			count++;
			search(queue[now_count + 1][0], queue[now_count + 1][1], next_day, now_count + 1);
		}
	}
	else {
		search(queue[now_count+1][0], queue[now_count+1][1], next_day, now_count + 1);
	}
}

int main(void) {
	int isallmo = 0;
	scanf("%d %d", &m, &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &arr[i][j]);
			if (arr[i][j] == 1) {
				queue[queue_size][0] = i;
				queue[queue_size++][1] = j;
			}
			if (arr[i][j] == 0) {
				isallmo = 1;
			}
		}
	}
	if (isallmo == 0) {
		printf("0");
	}
	else {
		if (queue_size > 0) {
			search(queue[0][0], queue[0][1], queue_size, 0);
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (arr[i][j] == 0) {
						printf("-1");
						return 0;
					}
				}
			}
			printf("%d", count);
		}
		else {
			if (isallmo == 0) {
				printf("0");
			}
			else {
				printf("-1");
			}
		}
	}
	return 0;
}