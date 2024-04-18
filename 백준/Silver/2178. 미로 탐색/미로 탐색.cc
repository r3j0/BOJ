#include <stdio.h>

char map[105][105];

int queue1[10000][2] = {0,};
int queue2[10000][2] = {0,};
int queue1_num = 0;
int queue2_num = 0;
int queue_mode = 1;

int visit[105][105] = {0,};

int row[4] = {-1, 1, 0, 0};
int col[4] = {0, 0, -1, 1};

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);	
	for(int i = 0; i < n; i++)
		scanf("%s", map[i]);
	
	queue1[queue1_num][0] = 0;
	queue1[queue1_num][1] = 0;
	queue1_num += 1;
	visit[0][0] = 1;
	
	int time = 0;
	while(1) {
		int size;
		if(queue_mode == 1) size = queue1_num;
		else size = queue2_num;
		
		if(size == 0) break;
		
		int done = 0;
		for(int s = 0; s < size; s++) {
			int y, x;
			if(queue_mode == 1) {
				y = queue1[s][0];
				x = queue1[s][1];
			}
			else {
				y = queue2[s][0];
				x = queue2[s][1];
			}
			
			if(y == n - 1 && x == m - 1) {
				done = 1;
				break;
			}
			
			
			for(int d = 0; d < 4; d++) {
				int ny = y + row[d];
				int nx = x + col[d];
				
				if(0 <= ny && ny < n && 0 <= nx && nx < m && visit[ny][nx] == 0 && map[ny][nx] == '1') {
					visit[ny][nx] = 1;
					
					if(queue_mode == 1) {
						queue2[queue2_num][0] = ny;
						queue2[queue2_num++][1] = nx;
					}
					else {
						queue1[queue1_num][0] = ny;
						queue1[queue1_num++][1] = nx;
					}
				}
			}
		}
		if(done == 1) break;
		
		time += 1;
		if(queue_mode == 1) {
			queue_mode = 2;
			queue1_num = 0;
		}
		else {
			queue_mode = 1;
			queue2_num = 0;
		}
	}
	
	printf("%d", time + 1);
	return 0;
}