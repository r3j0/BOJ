#include <stdio.h>

int sizelen(char* s) {
	int len = 0;
	while (1) {
		if (s[len] == '\0') {
			break;
		}
		len++;
	}
	return len;
}

int main(void) {
	int c;
	int g[1000];
	char str[1000][20];

	scanf("%d", &c);
	for (int i = 0; i < c; i++) {
		scanf("%d %s", &g[i], str[i]);
		for (int j = 0; j < sizelen(str[i]); j++) {
			for (int n = 0; n < g[i]; n++) {
				printf("%c", str[i][j]);
			}
		}
		printf("\n");
	}
	return 0;
}