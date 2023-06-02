#include <stdio.h>
#include <math.h>
#define SIZE 100001
typedef long long LL;

int arr[SIZE];

typedef struct _Node {
	LL max;
	LL min;
	LL sums;

	LL sumLazy;
	LL sqrtLazy;
} node;

node tree[SIZE * 4];

node merge(node a, node b) {
	node tmp;
	if (a.max > b.max)
		tmp.max = a.max;
	else
		tmp.max = b.max;

	if (a.min < b.min)
		tmp.min = a.min;
	else
		tmp.min = b.min;

	tmp.sums = a.sums + b.sums;
	tmp.sumLazy = 0;
	tmp.sqrtLazy = 0;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].max = arr[start];
		tree[idx].min = arr[start];

		tree[idx].sums = arr[start];
		tree[idx].sumLazy = 0;
		tree[idx].sqrtLazy = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void push(int start, int end, int idx) {
	if(tree[idx].sumLazy != 0 || tree[idx].sqrtLazy != 0) {
		if (tree[idx].sqrtLazy == 0) {
			tree[idx].max += tree[idx].sumLazy;
			tree[idx].min += tree[idx].sumLazy;
			tree[idx].sums += (end - start + 1) * tree[idx].sumLazy;

			if (start != end) {
				tree[idx * 2].sumLazy += tree[idx].sumLazy;
				tree[idx * 2 + 1].sumLazy += tree[idx].sumLazy;
			}
		}
		else {
			tree[idx].max = tree[idx].sqrtLazy + tree[idx].sumLazy;
			tree[idx].min = tree[idx].sqrtLazy + tree[idx].sumLazy;
			tree[idx].sums = (end - start + 1) * (tree[idx].sqrtLazy + tree[idx].sumLazy);

			if (start != end) {
				tree[idx * 2].sumLazy = tree[idx].sumLazy;
				tree[idx * 2].sqrtLazy = tree[idx].sqrtLazy;
				tree[idx * 2 + 1].sumLazy = tree[idx].sumLazy;
				tree[idx * 2 + 1].sqrtLazy = tree[idx].sqrtLazy;
			}
		}
	}	

	tree[idx].sumLazy = 0;
	tree[idx].sqrtLazy = 0;
}

void update_sums(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].sumLazy = value;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_sums(start, mid, idx * 2, left, right, value);
	update_sums(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void update_sqrt(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		if(floor(sqrt(tree[idx].min)) == floor(sqrt(tree[idx].max))) {
			tree[idx].sqrtLazy = floor(sqrt(tree[idx].max));
			push(start, end, idx);
			return;
		}
		if (tree[idx].min + 1 == tree[idx].max) {
			tree[idx].sumLazy = floor(sqrt(tree[idx].min)) - tree[idx].min;
			push(start, end, idx);
			return;
		}
	}

	int mid = (start + end) / 2;
	update_sqrt(start, mid, idx * 2, left, right);
	update_sqrt(mid + 1, end, idx * 2 + 1, left, right);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

LL getSums(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx].sums;

	int mid = (start + end) / 2;
	return getSums(start, mid, idx * 2, left, right) + getSums(mid + 1, end, idx * 2 + 1, left, right);
}
int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

	init(0, n - 1, 1);

	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		int mode, l, r;
		scanf("%d %d %d", &mode, &l, &r);
		if (mode == 1) {
			int x;
			scanf("%d", &x);
			update_sums(0, n - 1, 1, l - 1, r - 1, x);
		}
		else if (mode == 2) {
			update_sqrt(0, n - 1, 1, l - 1, r - 1);
		}
		else printf("%lld\n", getSums(0, n - 1, 1, l - 1, r - 1));
	}

	return 0;
}