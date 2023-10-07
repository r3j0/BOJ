#include <stdio.h>
#include <string.h>

char str[1000001];
int main(void) {
	scanf("%s", str);
	int cnt = 1;
	while (cnt < strlen(str)) {
		if (str[cnt] != str[0]) break;
		cnt += 1;
	}
	printf("%d", cnt);
	return 0;
}