#include <stdio.h>
#define SIZE 200005

typedef struct _Node {
	int lMax;
	int rMax;
	int allMax;
	int cnt;
} Node;
Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;
	if (a.lMax == a.cnt) {
		if (a.lMax > a.cnt + b.lMax) tmp.lMax = a.lMax;
		else tmp.lMax = a.cnt + b.lMax;
	}
	else tmp.lMax = a.lMax;

	if (b.rMax == b.cnt) {
		if (b.rMax > b.cnt + a.rMax) tmp.rMax = b.rMax;
		else tmp.rMax = b.cnt + a.rMax;
	}
	else tmp.rMax = b.rMax;

	if (a.allMax >= b.allMax && a.allMax >= a.rMax + b.lMax) tmp.allMax = a.allMax;
	else if (b.allMax >= a.allMax && b.allMax >= a.rMax + b.lMax) tmp.allMax = b.allMax;
	else tmp.allMax = a.rMax + b.lMax;

	tmp.cnt = a.cnt + b.cnt;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].lMax = 0;
		tree[idx].rMax = 0;
		tree[idx].allMax = 0;
		tree[idx].cnt = 1;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void reverse(int start, int end, int idx, int what) {
	if (what < start || end < what) return;
	if (start == end) {
		int now = !(tree[idx].allMax);
		tree[idx].lMax = now;
		tree[idx].rMax = now;
		tree[idx].allMax = now;
		return;
	}

	int mid = (start + end) / 2;
	reverse(start, mid, idx * 2, what);
	reverse(mid + 1, end, idx * 2 + 1, what);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

int main(void) {
	int n, q;
	scanf("%d %d", &n, &q);
	if (n == 1) {
		int tmp;
		for (int i = 0; i < q; i++) {
			scanf("%d", &tmp);
			printf("1\n");
		}
	}
	else {
		init(0, n - 1, 1);

		for (int i = 0; i < q; i++) {
			int num;
			scanf("%d", &num);
			if (num - 2 >= 0) reverse(0, n - 1, 1, num - 2);
			if (num - 1 < n - 2) reverse(0, n - 1, 1, num - 1);
			if (tree[1].lMax >= tree[1].rMax && tree[1].lMax >= tree[1].allMax) printf("%d\n", tree[1].lMax + 1);
			else if (tree[1].rMax >= tree[1].lMax && tree[1].rMax >= tree[1].allMax) printf("%d\n", tree[1].rMax + 1);
			else printf("%d\n", tree[1].allMax + 1);
		}

	}
	return 0;
}