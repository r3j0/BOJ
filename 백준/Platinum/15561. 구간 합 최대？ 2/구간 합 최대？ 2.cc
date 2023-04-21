#include <stdio.h>
#define SIZE 100001
typedef long long LL;

int arr[SIZE];
typedef struct _Node {
	LL lMax;
	int lMaxIdx[2];
	LL rMax;
	int rMaxIdx[2];
	LL allMax;
	int allMaxIdx[2];
	LL sums;
} Node;
Node tree[SIZE * 4];

int n, q, u, v;

LL mq(LL sums, LL i, LL j) { return (u * sums) + (v * (j - i)); }

Node merge(Node a, Node b) {
	Node tmp;
	if (mq(a.lMax, a.lMaxIdx[0], a.lMaxIdx[1]) > mq(a.sums + b.lMax, a.lMaxIdx[0], b.lMaxIdx[1])) {
		tmp.lMax = a.lMax;
		tmp.lMaxIdx[0] = a.lMaxIdx[0];
		tmp.lMaxIdx[1] = a.lMaxIdx[1];
	}
	else {
		tmp.lMax = a.sums + b.lMax;
		tmp.lMaxIdx[0] = a.lMaxIdx[0];
		tmp.lMaxIdx[1] = b.lMaxIdx[1];
	}

	if (mq(b.rMax, b.rMaxIdx[0], b.rMaxIdx[1]) > mq(a.rMax + b.sums, a.rMaxIdx[0], b.rMaxIdx[1])) {
		tmp.rMax = b.rMax;
		tmp.rMaxIdx[0] = b.rMaxIdx[0];
		tmp.rMaxIdx[1] = b.rMaxIdx[1];
	}
	else {
		tmp.rMax = a.rMax + b.sums;
		tmp.rMaxIdx[0] = a.rMaxIdx[0];
		tmp.rMaxIdx[1] = b.rMaxIdx[1];
	}

	LL q1 = mq(a.allMax, a.allMaxIdx[0], a.allMaxIdx[1]);
	LL q2 = mq(b.allMax, b.allMaxIdx[0], b.allMaxIdx[1]);
	LL q3 = mq(a.rMax + b.lMax, a.rMaxIdx[0], b.lMaxIdx[1]);

	if (q1 >= q2 && q1 >= q3) {
		tmp.allMax = a.allMax;
		tmp.allMaxIdx[0] = a.allMaxIdx[0];
		tmp.allMaxIdx[1] = a.allMaxIdx[1];
	}
	else if (q2 >= q1 && q2 >= q3) {
		tmp.allMax = b.allMax;
		tmp.allMaxIdx[0] = b.allMaxIdx[0];
		tmp.allMaxIdx[1] = b.allMaxIdx[1];
	}
	else {
		tmp.allMax = a.rMax + b.lMax;
		tmp.allMaxIdx[0] = a.rMaxIdx[0];
		tmp.allMaxIdx[1] = b.lMaxIdx[1];
	}

	tmp.sums = a.sums + b.sums;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].lMax = arr[start];
		tree[idx].lMaxIdx[0] = start;
		tree[idx].lMaxIdx[1] = start;
		tree[idx].rMax = arr[start];
		tree[idx].rMaxIdx[0] = start;
		tree[idx].rMaxIdx[1] = start;
		tree[idx].allMax = arr[start];
		tree[idx].allMaxIdx[0] = start;
		tree[idx].allMaxIdx[1] = start;
		tree[idx].sums = arr[start];
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void update(int start, int end, int idx, int what, int value) {
	if (what < start || end < what) return;
	if (start == end) {
		tree[idx].lMax = value;
		tree[idx].rMax = value;
		tree[idx].allMax = value;
		tree[idx].sums = value;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

Node interval_max(int start, int end, int idx, int left, int right, int* error) {
	Node tmp;
	if (end < left || right < start) {
		*error = 1;
		return tmp;
	}
	if (left <= start && end <= right) {
		*error = 0;
		return tree[idx];
	}

	int mid = (start + end) / 2;
	int e1 = 0;
	Node q1 = interval_max(start, mid, idx * 2, left, right, &e1);
	int e2 = 0;
	Node q2 = interval_max(mid + 1, end, idx * 2 + 1, left, right, &e2);

	if (e1 == 1 && e2 == 1) {
		*error = 1;
		return tmp;
	}
	*error = 0;
	if (e1 == 1) return q2;
	if (e2 == 1) return q1;

	tmp = merge(q1, q2);
	return tmp;
}

LL max3(LL a, LL b, LL c) {
	return (a >= b && a >= c) ? a : ((b >= a && b >= c) ? b : c);
}

void tree_debug(int start, int end, int idx) {
	if (start == end) {
		printf("[%d]\n", start);
		printf("lMax : %lld ( %d - %d )\n", tree[idx].lMax, tree[idx].lMaxIdx[0], tree[idx].lMaxIdx[1]);
		printf("rMax : %lld ( %d - %d )\n", tree[idx].rMax, tree[idx].rMaxIdx[0], tree[idx].rMaxIdx[1]);
		printf("allMax : %lld ( %d - %d )\n\n", tree[idx].allMax, tree[idx].allMaxIdx[0], tree[idx].allMaxIdx[1]);
		return;
	}

	printf("[%d-%d]\n", start, end);
	printf("lMax : %lld ( %d - %d )\n", tree[idx].lMax, tree[idx].lMaxIdx[0], tree[idx].lMaxIdx[1]);
	printf("rMax : %lld ( %d - %d )\n", tree[idx].rMax, tree[idx].rMaxIdx[0], tree[idx].rMaxIdx[1]);
	printf("allMax : %lld ( %d - %d )\n", tree[idx].allMax, tree[idx].allMaxIdx[0], tree[idx].allMaxIdx[1]);

	int mid = (start + end) / 2;
	tree_debug(start, mid, idx * 2);
	tree_debug(mid + 1, end, idx * 2 + 1);
}
int main(void) {	
	scanf("%d %d %d %d", &n, &q, &u, &v);

	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
	init(0, n - 1, 1);
	//tree_debug(0, n - 1, 1);

	for (int i = 0; i < q; i++) {
		int c, a, b;
		scanf("%d %d %d", &c, &a, &b);

		if (c == 0) {
			int e;
			Node result = interval_max(0, n - 1, 1, a - 1, b - 1, &e);
			LL q1 = mq(result.lMax, result.lMaxIdx[0], result.lMaxIdx[1]);
			LL q2 = mq(result.rMax, result.rMaxIdx[0], result.rMaxIdx[1]);
			LL q3 = mq(result.allMax, result.allMaxIdx[0], result.allMaxIdx[1]);

			if (q1 >= q2 && q1 >= q3) printf("%lld\n", q1);
			else if (q2 >= q1 && q2 >= q3) printf("%lld\n", q2);
			else printf("%lld\n", q3);
		}
		else {
			update(0, n - 1, 1, a - 1, b);
			//tree_debug(0, n - 1, 1);
		}
	}

	return 0;
}