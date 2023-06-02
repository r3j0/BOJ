#include <stdio.h>
#include <math.h>
#define SIZE 200002
typedef long long LL;

LL arr[SIZE];

typedef struct _Node {
	LL max;
	LL min;
	LL sums;

	LL sumLazy;
	int sumLazyOn;
	LL divLazy;
	int divLazyOn;
} Node;
Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;
	if (a.max > b.max) tmp.max = a.max;
	else tmp.max = b.max;

	if (a.min < b.min) tmp.min = a.min;
	else tmp.min = b.min;

	tmp.sums = a.sums + b.sums;

	tmp.sumLazy = 0;
	tmp.sumLazyOn = 0;
	tmp.divLazy = 0;
	tmp.divLazyOn = 0;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].max = arr[start];
		tree[idx].min = arr[start];
		tree[idx].sums = arr[start];
		tree[idx].sumLazy = 0;
		tree[idx].sumLazyOn = 0;
		tree[idx].divLazy = 0;
		tree[idx].divLazyOn = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void push(int start, int end, int idx) {
	if (tree[idx].sumLazyOn != 0 || tree[idx].divLazyOn != 0) {
		if (tree[idx].divLazyOn == 0) {
			tree[idx].max += tree[idx].sumLazy;
			tree[idx].min += tree[idx].sumLazy;
			tree[idx].sums += (end - start + 1) * tree[idx].sumLazy;

			if (start != end) {
				tree[idx * 2].sumLazy += tree[idx].sumLazy;
				tree[idx * 2].sumLazyOn = 1;
				tree[idx * 2 + 1].sumLazy += tree[idx].sumLazy;
				tree[idx * 2 + 1].sumLazyOn = 1;
			}
		}
		else {
			tree[idx].max = tree[idx].divLazy + tree[idx].sumLazy;
			tree[idx].min = tree[idx].divLazy + tree[idx].sumLazy;
			tree[idx].sums = (end - start + 1) * (tree[idx].divLazy + tree[idx].sumLazy);

			if (start != end) {
				tree[idx * 2].sumLazy = tree[idx].sumLazy;
				tree[idx * 2].sumLazyOn = 1;
				tree[idx * 2].divLazy = tree[idx].divLazy;
				tree[idx * 2].divLazyOn = 1;
				tree[idx * 2 + 1].sumLazy = tree[idx].sumLazy;
				tree[idx * 2 + 1].sumLazyOn = 1;
				tree[idx * 2 + 1].divLazy = tree[idx].divLazy;
				tree[idx * 2 + 1].divLazyOn = 1;
			}
		}
		tree[idx].sumLazy = 0;
		tree[idx].sumLazyOn = 0;
		tree[idx].divLazy = 0;
		tree[idx].divLazyOn = 0;

		//printf("push [%d-%d] max %lld min %lld sums %lld \n", start, end, tree[idx].max,tree[idx].min,tree[idx].sums);
	}
}

void update_sum(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].sumLazy = value;
		tree[idx].sumLazyOn = 1;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_sum(start, mid, idx * 2, left, right, value);
	update_sum(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void update_div(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right && floor(tree[idx].max / (double)value) == floor(tree[idx].min / (double)value)) {
		tree[idx].divLazy = (LL)(floor(tree[idx].max / (double)value));
		tree[idx].divLazyOn = 1;
		push(start, end, idx);
		return;
	}
	if (left <= start && end <= right && tree[idx].max - tree[idx].min == 1) {
		tree[idx].sumLazy += (LL)(floor(tree[idx].min / (double)value)) - tree[idx].min;
		tree[idx].sumLazyOn = 1;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_div(start, mid, idx * 2, left, right, value);
	update_div(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

LL interval_max(int start, int end, int idx, int left, int right, int* error) {
	push(start, end, idx);
	if (end < left || right < start) {
		*error = 1;
		return 0;
	}
	if (left <= start && end <= right) {
		*error = 0;
		return tree[idx].max;
	}

	int mid = (start + end) / 2;
	int e1 = 0;
	LL r1 = interval_max(start, mid, idx * 2, left, right, &e1);
	int e2 = 0;
	LL r2 = interval_max(mid + 1, end, idx * 2 + 1, left, right, &e2);

	*error = 0;
	if (e1 == 1 || e2 == 1) {
		if (e1 == 1) return r2;
		else return r1;
	}
	else {
		if (r1 > r2) return r1;
		else return r2;
	}
}

int main(void) {
	int n, q;
	scanf("%d %d", &n, &q);

	for (int i = 0; i < n; i++) scanf("%lld", &arr[i]);
	init(0, n - 1, 1);

	for (int i = 0; i < q; i++) {
		int mode, l, r, x;
		scanf("%d %d %d %d", &mode, &l, &r, &x);
		//printf("---------------------\n");

		if (mode == 0) {
			update_sum(0, n - 1, 1, l, r, x);
		}
		else if (mode == 1) {
			update_div(0, n - 1, 1, l, r, x);
		}
		else if (mode == 2) {
			int e;
			printf("%lld\n", interval_max(0, n - 1, 1, l, r, &e));
		}
	}
	return 0;
}