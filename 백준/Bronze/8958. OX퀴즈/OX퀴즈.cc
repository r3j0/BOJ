#include <stdio.h>
#include <string.h>

char str[85];
int main(void) {
	int t;
	scanf("%d", &t);
	
	for (int tc = 0; tc < t; tc++) {
		scanf("%s", str);
		
		int o = 0;
		int score = 0;
		for (int i = 0; i < strlen(str); i++) {
			if (str[i] == 'O') {
				o += 1;
				score += o;
			}
			else {
				o = 0;
			}
		}
		
		printf("%d\n", score);
	}
	return 0;
}