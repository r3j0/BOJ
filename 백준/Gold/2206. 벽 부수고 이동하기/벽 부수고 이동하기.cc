#include <stdio.h>

char map[1005][1005] = { 0, };
int visit[1005][1005][2] = { 0, };

int queue1[1500000][3] = { 0, };
int queue1Size = 0;

int queue2[1500000][3] = { 0, };
int queue2Size = 0;

int queueMode = 1;

int low[4] = { -1,1,0,0 };
int col[4] = { 0,0,-1,1 };

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%s", map[i]);

	int block = 1;
	int done = 0;

	queue1[queue1Size][0] = 0;
	queue1[queue1Size][1] = 0;
	queue1[queue1Size++][2] = 0;
	visit[0][0][0] = 1;

	while (1) {
		int size;
		if (queueMode == 1) 
			size = queue1Size;
		else 
			size = queue2Size;
		
		if (size == 0) {
			printf("-1");
			return 0;
		}

		/*
		if (queueMode == 1) {
			printf("Queue1 >>\n");
			for (int a = 0; a < size; a++) {
				printf("(%d, %d) [%d] / ", queue1[a][0], queue1[a][1], queue1[a][2]);
			}
			printf("\n");
		}
		else {
			printf("Queue2 >>\n");
			for (int a = 0; a < size; a++) {
				printf("(%d, %d) [%d] / ", queue2[a][0], queue2[a][1], queue2[a][2]);
			}
			printf("\n");
		}
		*/

		for (int q = 0; q < size; q++) {
			if (queueMode == 1) {
				int ny = queue1[q][0];
				int nx = queue1[q][1];
				int isBreak = queue1[q][2];

				if (nx == m - 1 && ny == n - 1) {
					done = 1;
					break;
				}

				for (int i = 0; i < 4; i++) {
					int cx = nx + col[i];
					int cy = ny + low[i];
					if (cx >= 0 && cy >= 0 && cx < m && cy < n) {
						//printf("(%d, %d)\n", cy, cx);
						if (isBreak == 0) {
							if (map[cy][cx] == '0' && visit[cy][cx][0] == 0) {
								visit[cy][cx][0] = 1;
								queue2[queue2Size][0] = cy;
								queue2[queue2Size][1] = cx;
								queue2[queue2Size++][2] = 0;
							}
							else if (map[cy][cx] == '1' && visit[cy][cx][1] == 0) { // '1'
								visit[cy][cx][1] = 1;
								queue2[queue2Size][0] = cy;
								queue2[queue2Size][1] = cx;
								queue2[queue2Size++][2] = 1;
							}
						}
						else {
							if (map[cy][cx] == '0' && visit[cy][cx][1] == 0) {
								visit[cy][cx][1] = 1;
								queue2[queue2Size][0] = cy;
								queue2[queue2Size][1] = cx;
								queue2[queue2Size++][2] = 1;
							}
						}
					}
				}
			}
			else { // 2
				int ny = queue2[q][0];
				int nx = queue2[q][1];
				int isBreak = queue2[q][2];

				if (nx == m - 1 && ny == n - 1) {
					done = 1;
					break;
				}

				for (int i = 0; i < 4; i++) {
					int cx = nx + col[i];
					int cy = ny + low[i];
					if (cx >= 0 && cy >= 0 && cx < m && cy < n) {
						//printf("(%d, %d)\n", cy, cx);
						if (isBreak == 0) {
							if (map[cy][cx] == '0' && visit[cy][cx][0] == 0) {
								visit[cy][cx][0] = 1;
								queue1[queue1Size][0] = cy;
								queue1[queue1Size][1] = cx;
								queue1[queue1Size++][2] = 0;
							}
							else if (map[cy][cx] == '1' && visit[cy][cx][1] == 0) { // '1'
								visit[cy][cx][1] = 1;
								queue1[queue1Size][0] = cy;
								queue1[queue1Size][1] = cx;
								queue1[queue1Size++][2] = 1;
							}
						}
						else {
							if (map[cy][cx] == '0' && visit[cy][cx][1] == 0) {
								visit[cy][cx][1] = 1;
								queue1[queue1Size][0] = cy;
								queue1[queue1Size][1] = cx;
								queue1[queue1Size++][2] = 1;
							}
						}
					}
				}
			}
		}

		if (done == 1) {
			break;
		}

		if (queueMode == 1) {
			queueMode = 2;
			queue1Size = 0;
		}
		else {
			queueMode = 1;
			queue2Size = 0;
		}
		block++;
	}
	printf("%d", block);
	return 0;
}