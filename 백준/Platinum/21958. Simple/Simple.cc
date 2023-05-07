#include <stdio.h>
#define SIZE 200001
typedef long long int LL;

int arr[SIZE];
typedef struct _Node {
	LL min0;
	LL min1;
	LL max0;
	LL max1;
	LL lazy;
} Node;
Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;
	if (a.min0 == -1 || b.min0 == -1) {
		if (a.min0 == -1 && b.min0 == -1) tmp.min0 = -1;
		else if (a.min0 != -1) tmp.min0 = a.min0;
		else tmp.min0 = b.min0;
	}
	else {
		if (a.min0 < b.min0) tmp.min0 = a.min0;
		else tmp.min0 = b.min0;
	}
	if (a.min1 == -1 || b.min1 == -1) {
		if (a.min1 == -1 && b.min1 == -1) tmp.min1 = -1;
		else if (a.min1 != -1) tmp.min1 = a.min1;
		else tmp.min1 = b.min1;
	}
	else {
		if (a.min1 < b.min1) tmp.min1 = a.min1;
		else tmp.min1 = b.min1;
	}
	if (a.max0 == -1 || b.max0 == -1) {
		if (a.max0 == -1 && b.max0 == -1) tmp.max0 = -1;
		else if (a.max0 != -1) tmp.max0 = a.max0;
		else tmp.max0 = b.max0;
	}
	else {
		if (a.max0 > b.max0) tmp.max0 = a.max0;
		else tmp.max0 = b.max0;
	}
	if (a.max1 == -1 || b.max1 == -1) {
		if (a.max1 == -1 && b.max1 == -1) tmp.max1 = -1;
		else if (a.max1 != -1) tmp.max1 = a.max1;
		else tmp.max1 = b.max1;
	}
	else {
		if (a.max1 > b.max1) tmp.max1 = a.max1;
		else tmp.max1 = b.max1;
	}
	tmp.lazy = 0;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		if (arr[start] % 2 == 0) {
			tree[idx].min0 = arr[start];
			tree[idx].max0 = arr[start];
			tree[idx].min1 = -1;
			tree[idx].max1 = -1;
		}
		else {
			tree[idx].min1 = arr[start];
			tree[idx].max1 = arr[start];
			tree[idx].min0 = -1;
			tree[idx].max0 = -1;
		}
		tree[idx].lazy = 0;
		return;
	}
	
	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

LL swap(LL* a, LL* b) {
	LL tmp = *a;
	*a = *b;
	*b = tmp;
}

void push(int start, int end, int idx) {
	if (tree[idx].lazy != 0) {
		if (tree[idx].min0 != -1) tree[idx].min0 += tree[idx].lazy;
		if (tree[idx].min1 != -1) tree[idx].min1 += tree[idx].lazy;
		if (tree[idx].max0 != -1) tree[idx].max0 += tree[idx].lazy;
		if (tree[idx].max1 != -1) tree[idx].max1 += tree[idx].lazy;
		
		if (tree[idx].lazy % 2 == 1) {
			swap(&tree[idx].min0, &tree[idx].min1);
			swap(&tree[idx].max0, &tree[idx].max1);
		}

		if (start != end) {
			tree[idx * 2].lazy += tree[idx].lazy;
			tree[idx * 2 + 1].lazy += tree[idx].lazy;
		}
		tree[idx].lazy = 0;
	}
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
Node interval(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	Node tmp;
	tmp.min0 = -1; tmp.min1 = -1;
	tmp.max0 = -1; tmp.max1 = -1;
	tmp.lazy = 0;

	if (end < left || right < start) return tmp;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	return merge(interval(start, mid, idx * 2, left, right), interval(mid + 1, end, idx * 2 + 1, left, right));
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
	init(0, n - 1, 1);

	int q;
	scanf("%d", &q);
	for (int i = 0; i < q; i++) {
		int mode;
		scanf("%d", &mode);
		if (mode == 0) {
			int a, b, val;
			scanf("%d %d %d", &a, &b, &val);
			update_range(0, n - 1, 1, a - 1, b - 1, val);
		}
		else {
			int a, b;
			scanf("%d %d", &a, &b);
			Node result = interval(0, n - 1, 1, a - 1, b - 1);
			printf("%lld %lld\n", result.min0, result.max1);
		}
	}
	return 0;
}