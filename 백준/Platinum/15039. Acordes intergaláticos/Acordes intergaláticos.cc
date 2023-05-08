#include <stdio.h>
#define SIZE 100001
typedef long long LL;

typedef struct _Node {
	int counts[9];
	LL lazy;
} Node;

Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;
	for (int i = 0; i < 9; i++) tmp.counts[i] = a.counts[i] + b.counts[i];
	tmp.lazy = 0;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		for (int i = 0; i < 9; i++) tree[idx].counts[i] = 0;
		tree[idx].counts[1] = 1;
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
		int tmp_counts[9] = { 0, };
		for (int i = 0; i < 9; i++)
			tmp_counts[(i + tree[idx].lazy) % 9] = tree[idx].counts[i];
		for (int i = 0; i < 9; i++)
			tree[idx].counts[i] = tmp_counts[i];
		if (start != end) {
			tree[idx * 2].lazy += tree[idx].lazy;
			tree[idx * 2 + 1].lazy += tree[idx].lazy;
		}
		tree[idx].lazy = 0;
	}
}

Node interval(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	Node tmp;
	for (int i = 0; i < 9; i++) tmp.counts[i] = 0;
	tmp.lazy = 0;
	if (end < left || right < start) return tmp;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	Node q1 = interval(start, mid, idx * 2, left, right);
	Node q2 = interval(mid + 1, end, idx * 2 + 1, left, right);
	return merge(q1, q2);
}

void update_range(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].lazy += value;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right, value);
	update_range(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void tree_debug(int start, int end, int idx) {
	push(start, end, idx);
	if (start == end) {
		/*
		printf("[%d-%d] ", start, end);
		for (int i = 0; i < 9; i++) {
			printf("(%d) %d ", i, tree[idx].counts[i]);
		}
		printf("\n");
		*/
		for (int i = 0; i < 9; i++) {
			if (tree[idx].counts[i] == 1) {
				printf("%d\n", i);
				break;
			}
		}
		return;
	}

	int mid = (start + end) / 2;
	tree_debug(start, mid, idx * 2);
	tree_debug(mid + 1, end, idx * 2 + 1);
}

int main(void) {
	int n, q;
	scanf("%d %d", &n, &q);
	init(0, n - 1, 1);

	for (int i = 0; i < q; i++) {
		//tree_debug(0, n - 1, 1);
		int a, b;
		scanf("%d %d", &a, &b);
		Node im = interval(0, n - 1, 1, a, b);
		int max = 0;
		for (int k = 1; k < 9; k++) {
			if (im.counts[k] >= im.counts[max]) max = k;
		}
		//printf("%d\n", max);
		update_range(0, n - 1, 1, a, b, max);
	}

	tree_debug(0, n - 1, 1);
	return 0;
}