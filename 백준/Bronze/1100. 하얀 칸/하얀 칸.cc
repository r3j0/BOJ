#include <stdio.h>

int main(void) {
	char map[8][10];
	
	int cnt = 0;
	for (int i = 0; i < 8; i++) {
		scanf("%s", map[i]);
		
		if(i % 2 == 0) {
			for(int j = 0; j < 8; j += 2) {
				if (map[i][j] == 'F') cnt += 1;
			}
		}
		else {
			for(int j = 1; j < 8; j += 2) {
				if (map[i][j] == 'F') cnt += 1; 
			}
		}
	}
	
	printf("%d", cnt);
	return 0;
	
}