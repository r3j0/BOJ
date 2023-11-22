#include <stdio.h>

int hans(int n) {
	int j[4];
	if (n < 10) {
		return 1;
	}
	else if (n < 100) {
		return 1;
	}
	else if (n < 1000) {
		j[0] = n / 100;
		j[1] = n % 100 / 10;
		j[2] = n % 10;
		if (j[0] - j[1] == j[1] - j[2])
			return 1;
		else
			return 0;
	}
	else {
		return 0;
	}
}

int main(void) {
	int num;
	int result = 0;
	scanf("%d", &num);
	for (int i = 1; i <= num; i++) {
		result += hans(i);
	}
	printf("%d", result);
	return 0;
}