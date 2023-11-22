#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int n;
	char str[102];
	int cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int lap[26] = { 0, };
		int no = 0;
		scanf("%s", str);
		for (int j = 0; j < strlen(str); j++) {
			if (j != 0) {
				if (lap[str[j] - 97] > 0 && str[j-1] != str[j]) {
					no = 1;
				}
				else {
					lap[str[j] - 97]++;
				}
			}
			else {
				lap[str[j] - 97]++;
			}
		}
		if (no == 0)
			cnt++;
	}
	printf("%d", cnt);
	return 0;
}