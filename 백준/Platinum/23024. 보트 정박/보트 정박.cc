#include <stdio.h>
#define SIZE 200004
typedef unsigned long long LL;

LL arr[SIZE];
LL tree[SIZE * 4][2];

LL max(LL a, LL b) {
	if (a > b) return a;
	else return b;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx][0] = arr[start];
		tree[idx][1] = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx][0] = max(tree[idx * 2][0], tree[idx * 2 + 1][0]);
	tree[idx][1] = tree[idx * 2][1] + tree[idx * 2 + 1][1];
}

int find(int start, int end, int idx, LL now, int numb) {
	if (tree[idx][0] < now) return 0;
	if (start == end) {
		tree[idx][0] = 0;
		tree[idx][1] = (LL)((LL)numb * (LL)(start + 1));
		return 1;
	}

	int mid = (start + end) / 2;
	int d = 0;
	d = find(start, mid, idx * 2, now, numb);
	if (d == 1) {
		tree[idx][0] = max(tree[idx * 2][0], tree[idx * 2 + 1][0]);
		tree[idx][1] = tree[idx * 2][1] + tree[idx * 2 + 1][1];
		return d;
	}

	d = find(mid + 1, end, idx * 2 + 1, now, numb);
	tree[idx][0] = max(tree[idx * 2][0], tree[idx * 2 + 1][0]);
	tree[idx][1] = tree[idx * 2][1] + tree[idx * 2 + 1][1];
	return d;
}

int main(void) {
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++) {
		int n, m; 
		scanf("%d %d", &n, &m);

		for (int i = 0; i < n; i++) 
			scanf("%llu", &arr[i]);
		init(0, n - 1, 1);

		for (int i = 0; i < m; i++) {
			LL now; 
			scanf("%llu", &now);
			find(0, n - 1, 1, now, i + 1);
		}
		printf("%llu\n", tree[1][1]);
	}
	return 0;
}