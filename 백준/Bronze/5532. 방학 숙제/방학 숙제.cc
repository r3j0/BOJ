#include <stdio.h>

int main(void) {
	int l, a, b, c, d;
	scanf("%d", &l);
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	scanf("%d", &d);
	printf("%d", l - (((a / c) + (a % c == 0 ? 0 : 1))>((b / d) + (b % d == 0 ? 0 : 1))? ((a / c) + (a % c == 0 ? 0 : 1)): ((b / d) + (b % d == 0 ? 0 : 1))));
	return 0;
}