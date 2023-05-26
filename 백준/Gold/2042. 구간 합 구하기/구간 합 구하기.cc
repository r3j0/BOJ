#include <stdio.h>
#define SIZE 1000000
typedef long long LL;

LL arr[SIZE];
LL tree[SIZE * 4];

void build(int start, int end, int idx) {
	if(start == end) {
		tree[idx] = arr[start];
		return;
	}

	int mid = (start + end) / 2;
	build(start, mid, idx * 2);
	build(mid + 1, end, idx * 2 + 1);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

void update(int start, int end, int idx, LL what, LL value) {
	if(what < start || end < what) return;
	if (start == end) {
		tree[idx] = value;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

LL interval_sum(int start, int end, int idx, LL left, LL right) {
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	return interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right);
}

int main(void) {
	int n, m, k;
	scanf("%d %d %d", &n, &m, &k);

	for (int i = 0; i < n; i++) 
		scanf("%lld", &arr[i]);

	build(0, n - 1, 1);

	for (int i = 0; i < m + k; i++) {
		LL a, b, c;
		scanf("%lld %lld %lld", &a, &b, &c);
		if (a == 1) {
			update(0, n - 1, 1, b - 1, c);
		}
		else {
			printf("%lld\n", interval_sum(0, n - 1, 1, b - 1, c - 1));
		}
	}
	return 0;
}