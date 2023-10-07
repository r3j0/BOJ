#include <stdio.h>
#include <string.h>

char str[50][51];
int main(void) {
	int n; scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%s", str[i]);
	
	char result[51];
	for (int i = 0; i < strlen(str[0]); i++) {
		// i번째 문자 패턴 찾기
		for (int j = 1; j < n; j++) {
			if (str[j][i] != str[0][i]) {
				// 0번째 문자열의 i번째 문자와 j번째 문자열의 i번째 문자가 다르면 ?
				result[i] = '?';
				break;
			}
		}

		if (result[i] != '?') result[i] = str[0][i];
	}
	result[strlen(str[0])] = 0;

	printf("%s", result);
	return 0;
}