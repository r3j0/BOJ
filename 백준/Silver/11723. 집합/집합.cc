#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int arr[30] = { 0, };

void add(int x) {
	arr[x] = 1;
}

void rem(int x) {
	arr[x] = 0;
}

void check(int x) {
	if (arr[x] == 1)
		printf("1\n");
	else
		printf("0\n");
}

void toggle(int x) {
	if (arr[x] == 1)
		rem(x);
	else
		add(x);
}
void all() {
	for (int i = 1; i <= 20; i++)
		add(i);
}
void empty() {
	for (int i = 1; i <= 20; i++)
		rem(i);

}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char ins[10] = { 0, };
		scanf("%s", ins);
		if (!strcmp("add", ins)) {
			int insnum = 0;
			scanf("%d", &insnum);
			add(insnum);
		}
		else if (!strcmp("remove", ins)) {
			int insnum = 0;
			scanf("%d", &insnum);
			rem(insnum);
		}
		else if (!strcmp("check", ins)) {
			int insnum = 0;
			scanf("%d", &insnum);
			check(insnum);
		}
		else if (!strcmp("toggle", ins)) {
			int insnum = 0;
			scanf("%d", &insnum);
			toggle(insnum);
		}
		else if (!strcmp("all", ins)) {
			all();
		}
		else if (!strcmp("empty", ins)) {
			empty();
		}
		else {
			break;
		}
	}
	return 0;
}