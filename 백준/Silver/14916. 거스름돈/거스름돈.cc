#include <stdio.h>

int main(void) {
	int n;
	int done = 0;
	scanf("%d", &n);
	int s5 = (n - (n % 5)) / 5;
	while (s5 >= 0) {
		if ((n - (5 * s5)) % 2 == 0) {
			int s2 = (n - (5 * s5)) / 2;
			printf("%d", s5 + s2);
			done = 1;
			break;
		}
		s5--;
	}
	if (done == 0)
		printf("-1");
	return 0;
}