#include <stdio.h>
#define SIZE 2000001
typedef long long LL;

typedef struct Node {
	LL max;
	LL min;
	LL lazy;
	int lazyOn;
} Node;

Node tree[SIZE * 4];

void merge(int start, int end, int idx) {
	if (tree[idx * 2].max > tree[idx * 2 + 1].max) {
		tree[idx].max = tree[idx * 2].max;
	}
	else {
		tree[idx].max = tree[idx * 2 + 1].max;
	}

	if (tree[idx * 2].min < tree[idx * 2 + 1].min) {
		tree[idx].min = tree[idx * 2].min;
	}
	else {
		tree[idx].min = tree[idx * 2 + 1].min;
	}

	tree[idx].lazy = 0;
	tree[idx].lazyOn = 0;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].max = 0;
		tree[idx].min = 0;
		tree[idx].lazy = 0;
		tree[idx].lazyOn = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	merge(start, end, idx);
}

void push(int start, int end, int idx) {
	if (tree[idx].lazyOn != 0) {
		tree[idx].max = tree[idx].lazy;
		tree[idx].min = tree[idx].lazy;

		if (start != end) {
			tree[idx * 2].lazy = tree[idx].lazy;
			tree[idx * 2].lazyOn = 1;
			tree[idx * 2 + 1].lazy = tree[idx].lazy;
			tree[idx * 2 + 1].lazyOn = 1;
		}
		tree[idx].lazy = 0;
		tree[idx].lazyOn = 0;
	}
}

void update_range_add(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start || tree[idx].min >= value) return;
	if (left <= start && end <= right && tree[idx].max <= value) {
		tree[idx].max = value;
		tree[idx].min = value;
		
		if (start != end) {
			tree[idx * 2].lazy = value;
			tree[idx * 2].lazyOn = 1;
			tree[idx * 2 + 1].lazy = value;
			tree[idx * 2 + 1].lazyOn = 1;
		}

		return;
 	}

	int mid = (start + end) / 2;
	update_range_add(start, mid, idx * 2, left, right, value);
	update_range_add(mid + 1, end, idx * 2 + 1, left, right, value);
	merge(start, end, idx);
}
void update_range_minus(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start || tree[idx].max <= value) return;
	if (left <= start && end <= right && tree[idx].min >= value) {
		tree[idx].max = value;
		tree[idx].min = value;

		if (start != end) {
			tree[idx * 2].lazy = value;
			tree[idx * 2].lazyOn = 1;
			tree[idx * 2 + 1].lazy = value;
			tree[idx * 2 + 1].lazyOn = 1;
		}

		return;
	}
	int mid = (start + end) / 2;
	update_range_minus(start, mid, idx * 2, left, right, value);
	update_range_minus(mid + 1, end, idx * 2 + 1, left, right, value);
	merge(start, end, idx);
}

void print_tree(int start, int end, int idx) {
	push(start, end, idx);
	if (start == end) {
		printf("%lld\n", tree[idx].max);
		return;
	}

	int mid = (start + end) / 2;
	print_tree(start, mid, idx * 2);
	print_tree(mid + 1, end, idx * 2 + 1);
}

int main(void) {
	int n, k;
	scanf("%d %d", &n, &k);

	for (int i = 0; i < k; i++) {
		int op, left, right, height;
		scanf("%d %d %d %d", &op, &left, &right, &height);

		if (op == 1) update_range_add(0, n - 1, 1, left, right, height);
		else update_range_minus(0, n - 1, 1, left, right, height);
	}
	print_tree(0, n - 1, 1);
	return 0;
}