#include <stdio.h>

int main(void) {
	int x, y, w, h;
	int min;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	// 1. left
	min = x;
	// 2. right
	if (min > w - x)
		min = w - x;
	// 3. up
	if (min > y)
		min = y;
	// 4. down
	if (min > h - y)
		min = h - y;

	printf("%d", min);
	return 0;
}