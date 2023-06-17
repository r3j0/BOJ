#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	char str[100000];
	int floor = 0;
	int stick = 0;
	scanf("%s", str);
	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == '(') {
			floor++;
		}
		else { // ')'
			floor--;
			if (str[i - 1] == '(') {
				stick += floor;
			}
			if (str[i - 1] == ')') {
				stick++;
			}
		}
	}
	printf("%d", stick);
	return 0;
}