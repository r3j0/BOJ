#include <stdio.h>
#define SIZE 250001
typedef long long LL;

char str[SIZE];
int arr[SIZE];
typedef struct _Node {
	LL sums;
	int counts[10];
	LL lazy;
} Node;
Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;

	tmp.sums = a.sums + b.sums;
	for (int i = 0; i < 10; i++) tmp.counts[i] = a.counts[i] + b.counts[i];
	tmp.lazy = 0;

	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		for (int i = 0; i < 10; i++) tree[idx].counts[i] = 0;
		tree[idx].counts[arr[start]] = 1;
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
		LL new_sums = 0;
		int new_counts[10];
		for (int i = 0; i < 10; i++) {
			new_sums += tree[idx].counts[i] * ((i + tree[idx].lazy) % 10);
			new_counts[((i + tree[idx].lazy) % 10)] = tree[idx].counts[i];
		}

		tree[idx].sums = new_sums;
		for (int i = 0; i < 10; i++) tree[idx].counts[i] = new_counts[i];

		if (start != end) {
			tree[idx * 2].lazy += tree[idx].lazy;
			tree[idx * 2 + 1].lazy += tree[idx].lazy;
		}

		tree[idx].lazy = 0;
	}
}

Node interval_sum(int start, int end, int idx, int left, int right) {
	Node tmp;
	tmp.sums = -1;
	for (int i = 0; i < 10; i++) tmp.counts[i] = 0;
	tmp.lazy = 0;

	push(start, end, idx);
	if (end < left || right < start) return tmp;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	Node q1 = interval_sum(start, mid, idx * 2, left, right);
	Node q2 = interval_sum(mid + 1, end, idx * 2 + 1, left, right);
	if (q1.sums < 0 || q2.sums < 0) {
		if (q1.sums >= 0) return q1;
		else return q2;
	}

	tmp = merge(q1, q2);
	return tmp;
}

void interval_inc(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		LL new_sums = 0;
		int new_counts[10];
		for (int i = 0; i < 10; i++) {
			new_sums += tree[idx].counts[i] * ((i + 1) % 10);
			new_counts[((i + 1) % 10)] = tree[idx].counts[i];
		}

		tree[idx].sums = new_sums;
		for (int i = 0; i < 10; i++) tree[idx].counts[i] = new_counts[i];

		if (start != end) {
			tree[idx * 2].lazy += 1;
			tree[idx * 2 + 1].lazy += 1;
		}

		return;
	}

	int mid = (start + end) / 2;
	interval_inc(start, mid, idx * 2, left, right);
	interval_inc(mid + 1, end, idx * 2 + 1, left, right);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);
	scanf("%s", str);
	for (int i = 0; i < n; i++) arr[i] = str[i] - '0';
	init(0, n - 1, 1);

	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		Node res = interval_sum(0, n - 1, 1, a - 1, b - 1);
		interval_inc(0, n - 1, 1, a - 1, b - 1);
		printf("%lld\n", res.sums);
	}

	return 0;
}