#include <stdio.h>
#include <string.h>
#define SIZE 4587521
typedef long long LL;

typedef struct _Node {
	int max;
	int min;
	LL lazy;
} Node;
Node tree[SIZE * 4];
int c, n, o;

Node merge(Node a, Node b) {
	Node tmp;
	if (a.max > b.max) tmp.max = a.max;
	else tmp.max = b.max;

	if (a.min < b.min) tmp.min = a.min;
	else tmp.min = b.min;
	tmp.lazy = 0;

	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].max = 0;
		tree[idx].min = 0;
		tree[idx].lazy = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void push(int start, int end, int idx) {
	if (tree[idx].lazy != 0) {
		tree[idx].max += tree[idx].lazy;
		tree[idx].min += tree[idx].lazy;

		if (start != end) {
			tree[idx * 2].lazy += tree[idx].lazy;
			tree[idx * 2 + 1].lazy += tree[idx].lazy;
		}

		tree[idx].lazy = 0;
	}
}

void change(int start, int end, int idx, int what, int value) {
	push(start, end, idx);
	if (what < start || end < what) return;
	if (start == end) {
		if (value > 0) {
			if (tree[idx].max + value <= n) {
				printf("%d\n", value);
				tree[idx].max += value;
				tree[idx].min += value;
			}
			else {
				printf("%d\n", n - tree[idx].max);
				tree[idx].max = n;
				tree[idx].min = n;
			}
		}
		else {
			if (tree[idx].min + value >= 0) {
				printf("%d\n", value);
				tree[idx].max += value;
				tree[idx].min += value;
			}
			else {
				printf("%d\n", 0 - tree[idx].min);
				tree[idx].max = 0;
				tree[idx].min = 0;
			}
		}
		return;
	}

	int mid = (start + end) / 2;
	change(start, mid, idx * 2, what, value);
	change(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

int groupMaxFind(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return -1;
	if (left <= start && end <= right) return tree[idx].max;

	int mid = (start + end) / 2;
	int q1 = groupMaxFind(start, mid, idx * 2, left, right);
	int q2 = groupMaxFind(mid + 1, end, idx * 2 + 1, left, right);
	if (q1 > q2) return q1;
	else return q2;
}
int groupMinFind(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return 10005;
	if (left <= start && end <= right) return tree[idx].min;

	int mid = (start + end) / 2;
	int q1 = groupMinFind(start, mid, idx * 2, left, right);
	int q2 = groupMinFind(mid + 1, end, idx * 2 + 1, left, right);
	if (q1 < q2) return q1;
	else return q2;
}

void interval_change(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].max += value;
		tree[idx].min += value;

		if (start != end) {
			tree[idx * 2].lazy += value;
			tree[idx * 2 + 1].lazy += value;
		}

		return;
	}

	int mid = (start + end) / 2;
	interval_change(start, mid, idx * 2, left, right, value);
	interval_change(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void groupchange(int left, int right, int value) {
	if (value > 0) {
		int res = groupMaxFind(0, c - 1, 1, left, right);
		if (res + value <= n) {
			interval_change(0, c - 1, 1, left, right, value);
			printf("%d\n", value);
		}
		else {
			interval_change(0, c - 1, 1, left, right, n - res);
			printf("%d\n", n - res);
		}
	}
	else {
		int res = groupMinFind(0, c - 1, 1, left, right);
		if (res + value >= 0) {
			interval_change(0, c - 1, 1, left, right, value);
			printf("%d\n", value);
		}
		else {
			interval_change(0, c - 1, 1, left, right, 0 - res);
			printf("%d\n", 0 - res);
		}
	}
}

int getVal(int start, int end, int idx, int what) {
	push(start, end, idx);
	if (what < start || end < what) return -1;
	if (start == end) return tree[idx].max;

	int mid = (start + end) / 2;
	int q1 = getVal(start, mid, idx * 2, what);
	int q2 = getVal(mid + 1, end, idx * 2 + 1, what);
	if (q1 != -1) return q1;
	else return q2;
}

int main(void) {
	scanf("%d %d %d", &c, &n, &o);

	init(0, c, 1);

	for (int i = 0; i < o; i++) {
		char op[20];
		scanf("%s", op);

		if (!strcmp(op, "change")) {
			int x, s;
			scanf("%d %d", &x, &s);
			change(0, c - 1, 1, x, s);
		}
		else if (!strcmp(op, "groupchange")) {
			int a, b, s;
			scanf("%d %d %d", &a, &b, &s);
			groupchange(a, b, s);
		}
		else { // state
			int x;
			scanf("%d", &x);
			printf("%d\n", getVal(0, c - 1, 1, x));
		}
	}
	return 0;
}