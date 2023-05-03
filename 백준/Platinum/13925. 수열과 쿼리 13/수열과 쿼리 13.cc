#include <stdio.h>
#define SIZE 100001
#define MOD 1000000007
typedef long long LL;

int arr[SIZE];
typedef struct _Node {
	LL sums;
	LL lazy_sum;
	int lazy_sum_on;
	LL lazy_mul;
	int lazy_mul_on;
	LL lazy_v;
	int lazy_v_on;
} Node;

Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;
	tmp.sums = (a.sums + b.sums) % MOD;
	tmp.lazy_sum = 0;
	tmp.lazy_sum_on = 0;
	tmp.lazy_mul = 0;
	tmp.lazy_mul_on = 0;
	tmp.lazy_v = 0;
	tmp.lazy_v_on = 0;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].sums = arr[start];
		tree[idx].lazy_sum = 0;
		tree[idx].lazy_sum_on = 0;
		tree[idx].lazy_mul = 0;
		tree[idx].lazy_mul_on = 0;
		tree[idx].lazy_v = 0;
		tree[idx].lazy_v_on = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void push(int start, int end, int idx) {
	if (tree[idx].lazy_v_on == 1) {
		tree[idx].sums = (LL)(tree[idx].lazy_v * (LL)(end - start + 1)) % MOD;
		if (start != end) {
			tree[idx * 2].lazy_v = tree[idx].lazy_v % MOD;
			tree[idx * 2].lazy_v_on = 1;
			tree[idx * 2].lazy_sum = 0;
			tree[idx * 2].lazy_sum_on = 0;
			tree[idx * 2].lazy_mul = 0;
			tree[idx * 2].lazy_mul_on = 0;

			tree[idx * 2 + 1].lazy_v = tree[idx].lazy_v % MOD;
			tree[idx * 2 + 1].lazy_v_on = 1;
			tree[idx * 2 + 1].lazy_sum = 0;
			tree[idx * 2 + 1].lazy_sum_on = 0;
			tree[idx * 2 + 1].lazy_mul = 0;
			tree[idx * 2 + 1].lazy_mul_on = 0;
		}
		tree[idx].lazy_v = 0;
		tree[idx].lazy_v_on = 0;
	}

	if (tree[idx].lazy_mul_on == 1) {
		tree[idx].sums = (LL)(tree[idx].sums * tree[idx].lazy_mul) % MOD;
		if (start != end) {
			if (tree[idx * 2].lazy_mul_on == 0)
				tree[idx * 2].lazy_mul = tree[idx].lazy_mul % MOD;
			else
				tree[idx * 2].lazy_mul = (LL)(tree[idx * 2].lazy_mul * tree[idx].lazy_mul) % MOD;
			tree[idx * 2].lazy_sum = (LL)(tree[idx * 2].lazy_sum * tree[idx].lazy_mul) % MOD;

			tree[idx * 2].lazy_mul_on = 1;

			if (tree[idx * 2 + 1].lazy_mul_on == 0)
				tree[idx * 2 + 1].lazy_mul = tree[idx].lazy_mul % MOD;
			else
				tree[idx * 2 + 1].lazy_mul = (LL)(tree[idx * 2 + 1].lazy_mul * tree[idx].lazy_mul) % MOD;
			tree[idx * 2 + 1].lazy_sum = (LL)(tree[idx * 2 + 1].lazy_sum * tree[idx].lazy_mul) % MOD;

			tree[idx * 2 + 1].lazy_mul_on = 1;
		}
		tree[idx].lazy_mul = 0;
		tree[idx].lazy_mul_on = 0;
	}

	if (tree[idx].lazy_sum_on == 1) {
		tree[idx].sums = (LL)(tree[idx].sums + (tree[idx].lazy_sum * (LL)(end - start + 1))) % MOD;
		if (start != end) {
			tree[idx * 2].lazy_sum = (LL)(tree[idx * 2].lazy_sum + tree[idx].lazy_sum) % MOD;
			tree[idx * 2].lazy_sum_on = 1;
			tree[idx * 2 + 1].lazy_sum = (LL)(tree[idx * 2 + 1].lazy_sum + tree[idx].lazy_sum) % MOD;
			tree[idx * 2 + 1].lazy_sum_on = 1;
		}
		tree[idx].lazy_sum = 0;
		tree[idx].lazy_sum_on = 0;
	}
}

void update_sum(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].lazy_sum = value;
		tree[idx].lazy_sum_on = 1;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_sum(start, mid, idx * 2, left, right, value);
	update_sum(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}
void update_mul(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].lazy_mul = value;
		tree[idx].lazy_mul_on = 1;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_mul(start, mid, idx * 2, left, right, value);
	update_mul(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}
void update_v(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].lazy_v = value;
		tree[idx].lazy_v_on = 1;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_v(start, mid, idx * 2, left, right, value);
	update_v(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

LL interval_sum(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx].sums;

	int mid = (start + end) / 2;
	return (interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right)) % MOD;
}

void tree_debug(int start, int end, int idx) {
	if (start == end) {
		printf("[%d] %lld - (sum %lld (%d) mul %lld (%d) v %lld (%d))\n", start, tree[idx].sums, tree[idx].lazy_sum, tree[idx].lazy_sum_on, tree[idx].lazy_mul, tree[idx].lazy_mul_on, tree[idx].lazy_v, tree[idx].lazy_v_on);
		return;
	}
	printf("[%d-%d] %lld - (sum %lld (%d) mul %lld (%d) v %lld (%d))\n", start, end, tree[idx].sums, tree[idx].lazy_sum, tree[idx].lazy_sum_on, tree[idx].lazy_mul, tree[idx].lazy_mul_on, tree[idx].lazy_v, tree[idx].lazy_v_on);
	int mid = (start + end) / 2;
	tree_debug(start, mid, idx * 2);
	tree_debug(mid + 1, end, idx * 2 + 1);
}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
	init(0, n - 1, 1);

	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		//tree_debug(0, n - 1, 1);
		int mode;
		scanf("%d", &mode);

		if (mode == 1) {
			int x, y, v;
			scanf("%d %d %d", &x, &y, &v);
			update_sum(0, n - 1, 1, x - 1, y - 1, v);
		}
		else if (mode == 2) {
			int x, y, v;
			scanf("%d %d %d", &x, &y, &v);
			if(v != 1) update_mul(0, n - 1, 1, x - 1, y - 1, v);
		}
		else if (mode == 3) {
			int x, y, v;
			scanf("%d %d %d", &x, &y, &v);
			update_v(0, n - 1, 1, x - 1, y - 1, v);
		}
		else { // mode == 4
			int x, y;
			scanf("%d %d", &x, &y);
			printf("%lld\n", interval_sum(0, n - 1, 1, x - 1, y - 1) % MOD);
		}
	}
	return 0;
}