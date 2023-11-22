#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char str[52];
int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", str);

		int go = 0;
		int done = 0;
		for (int j = 0; j < strlen(str); j++) {
			if (str[j] == '(') go += 1;
			else if (str[j] == ')') {
				if (go == 0) {
					done = 1;
					break;
				}
				go -= 1;
			}
		}
		if (done == 0 && go == 0) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}