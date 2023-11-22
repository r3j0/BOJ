#include <stdio.h>
#include <string.h>

int stack[100001];

int main(void) {
	int n;
	char command[6];
	int push_int;

	int start_stack = 0;
	int end_stack = 0; // start_stack <= [ stack ] < end_stack

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", command);
		if (!(strcmp(command, "push"))) {
			scanf("%d", &push_int);
			stack[end_stack] = push_int;
			end_stack++;
		}
		else if (!(strcmp(command, "pop"))) {
			if(end_stack - start_stack == 0) {
				printf("-1\n");
			}
			else {
				printf("%d\n", stack[start_stack]);
				stack[start_stack] = 0;
				start_stack++;
			}
		}
		else if (!(strcmp(command, "size"))) {
			printf("%d\n", end_stack - start_stack);
		}
		else if (!(strcmp(command, "empty"))) {
			if (end_stack - start_stack == 0)
				printf("1\n");
			else
				printf("0\n");
		}
		else if (!(strcmp(command, "front"))) {
			if (end_stack - start_stack == 0)
				printf("-1\n");
			else
				printf("%d\n", stack[start_stack]);
		}
		else if (!(strcmp(command, "back"))) {
			if (end_stack - start_stack == 0)
				printf("-1\n");
			else
				printf("%d\n", stack[end_stack-1]);
		}
	}
	return 0;
}