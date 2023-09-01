#include <stdio.h>

int main(void) {
	int h, m, t;
	scanf("%d %d", &h, &m);
	scanf("%d", &t);
	m += t;
	while (m >= 60) {
		m -= 60;
		h += 1;
	}
	if (h >= 24) {
		h -= 24;
	}
	printf("%d %d", h, m);
	return 0;
}