#include <stdio.h>
#include <string.h>
#define SIZE 10000

int stack[SIZE];
int stack_top = -1;

int stack_full() {
	if (stack_top == SIZE - 1) return 1;
	else return 0;
}

int stack_empty() {
	if (stack_top == -1) return 1;
	else return 0;
}

void push(int n) {
	stack[++stack_top] = n;
}

int pop() {
	if (!stack_empty()) return stack[stack_top--];
    else return -1;
}

int top() {
    if (!stack_empty()) return stack[stack_top];
    else return -1;
}

int main(void) {
	int num;
	char str[10];
	scanf("%d", &num); // get number of instruction
    
	for (int i = 0; i < num; i++) {
		scanf("%s", str); // get instruction
		if (!strcmp(str, "push")) {
	        int push_argu;
			scanf("%d", &push_argu);
			push(push_argu);
		}
		else if (!strcmp(str, "top")) printf("%d\n", top());
		else if (!strcmp(str, "empty")) printf("%d\n", stack_empty());
		else if (!strcmp(str, "size")) printf("%d\n", stack_top + 1);
		else if (!strcmp(str, "pop")) printf("%d\n", pop());
	}
	return 0;
}