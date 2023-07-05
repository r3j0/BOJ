#include <stdio.h>

char arr[30][30] = { 0, };
int r, c;
int max = 1;

int stack[30] = { 0, };
int stack_size = 0;

void dfs(int sero, int garo, int count, int ssize) {
	if (sero > 0) {
		int done = 0;
		int now = arr[sero - 1][garo] - 48;
		for (int i = 0; i < stack_size; i++) {
			if (now == stack[i]) {
				done = 1;
				break;
			}
		}
		if (done == 0) {
			stack[stack_size++] = now;
			dfs(sero - 1, garo, count + 1, stack_size);
		}
	}
	stack_size = ssize;
	if (sero < r - 1) {
		int done = 0;
		int now = arr[sero + 1][garo] - 48;
		for (int i = 0; i < stack_size; i++) {
			if (now == stack[i]) {
				done = 1;
				break;
			}
		}
		if (done == 0) {
			stack[stack_size++] = now;
			dfs(sero + 1, garo, count + 1, stack_size);
		}
	}
	stack_size = ssize;
	if (garo > 0) {
		int done = 0;
		int now = arr[sero][garo - 1] - 48;
		for (int i = 0; i < stack_size; i++) {
			if (now == stack[i]) {
				done = 1;
				break;
			}
		}
		if (done == 0) {
			stack[stack_size++] = now;
			dfs(sero, garo - 1, count + 1, stack_size);
		}
	}
	stack_size = ssize;
	if (garo < c - 1) {
		int done = 0;
		int now = arr[sero][garo + 1] - 48;
		for (int i = 0; i < stack_size; i++) {
			if (now == stack[i]) {
				done = 1;
				break;
			}
		}
		if (done == 0) {
			stack[stack_size++] = now;
			dfs(sero, garo + 1, count + 1, stack_size);
		}
	}
	stack_size = ssize;

	if (max < count)
		max = count;
}

int main(void) {
	scanf("%d %d", &r, &c);
	for (int i = 0; i < r; i++) {
		scanf("%s", arr[i]);
	}
	stack[stack_size++] = arr[0][0] - 48;
	dfs(0, 0, 1, stack_size);
	printf("%d", max);
	return 0;
}