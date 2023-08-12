#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	char S[100];
	scanf("%s", &S);

	int alpha[26];
	for (int i = 0; i < 26; i++) {
		alpha[i] = -1;
	}

	int cnt = 0;
	while (S[cnt] != '\0') {
		if (alpha[S[cnt] - 'a'] != -1) {
			cnt++;
			continue;
		}

		alpha[S[cnt] - 'a'] = cnt;
		cnt += 1;
	}

	for (int i = 0; i < 26; i++) {
		printf("%d ", alpha[i]);
	}




	return 0;
}