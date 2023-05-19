#include <stdio.h>
#define SIZE 100005
typedef long long LL;

int arr[SIZE];

typedef struct _Node {
	LL sums;
	LL lazy;
} Node;

Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;
	tmp.sums = a.sums + b.sums;
	tmp.lazy = 0;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].sums = arr[start];
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
		if (tree[idx].lazy == -1) {
			tree[idx].sums = 0;
			if (start != end) {
				tree[idx * 2].lazy = -1;
				tree[idx * 2 + 1].lazy = -1;
			}
			tree[idx].lazy = 0;
		}
		else {
			if (tree[idx].sums < tree[idx].lazy) {
				tree[idx].sums = 0;
				if (start != end) {
					tree[idx * 2].lazy = -1;
					tree[idx * 2 + 1].lazy = -1;
				}
				tree[idx].lazy = 0;
			}
			else {
				tree[idx].sums /= tree[idx].lazy;
				if (start != end) {
					if (tree[idx * 2].lazy == 0) tree[idx * 2].lazy = tree[idx].lazy;
					else if (tree[idx * 2].lazy > 0) tree[idx * 2].lazy *= tree[idx].lazy;

					if (tree[idx * 2 + 1].lazy == 0) tree[idx * 2 + 1].lazy = tree[idx].lazy;
					else if (tree[idx * 2 + 1].lazy > 0) tree[idx * 2 + 1].lazy *= tree[idx].lazy;
				}
				tree[idx].lazy = 0;
			}
		}
	}
}

void update(int start, int end, int idx, int what, int value) {
	push(start, end, idx);
	if (what < start || end < what) return;
	if (start == end) {
		tree[idx].sums = value;
		tree[idx].lazy = 0;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void update_range(int start, int end, int idx, int left, int right, int k) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].lazy = k;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right, k);
	update_range(mid + 1, end, idx * 2 + 1, left, right, k);
}

LL interval_sum(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx].sums;

	int mid = (start + end) / 2;
	return interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right);
}

int main(void) {
	int n, q, k;
	scanf("%d %d %d", &n, &q, &k);

	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
	init(0, n - 1, 1);

	for (int i = 0; i < q; i++) {
		int mode, a, b;
		scanf("%d %d %d", &mode, &a, &b);
		if (mode == 1)
			update(0, n - 1, 1, a - 1, b);
		else if (mode == 2)
			update_range(0, n - 1, 1, a - 1, b - 1, k);
		else if (mode == 3)
			printf("%lld\n", interval_sum(0, n - 1, 1, a - 1, b - 1));
	}

	return 0;
}