#include <stdio.h>

int main(void) {
	int a, b, c;
	int result;
	scanf("%d %d %d", &a, &b, &c);
	if (a == b && b == c)
		result = 10000 + (a * 1000);
	else if (a == b || b == c || a == c) {
		if (a == b)
			result = 1000 + (a * 100);
		else
			result = 1000 + (c * 100);
	}
	else {
		if (a < b) {
			if (b < c)
				result = c * 100;
			else
				result = b * 100;
		}
		else {
			if (a < c)
				result = c * 100;
			else
				result = a * 100;
		}
	}
	printf("%d", result);
	return 0;
}