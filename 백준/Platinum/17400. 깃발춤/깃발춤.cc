#include <stdio.h>
#define SIZE 300001
typedef long long LL;

int arr[SIZE];
LL tree[SIZE * 4][2];

void init(int start, int end, int idx) {
	if (start == end) {
		if (start % 2 == 0) {
			tree[idx][0] = arr[start];
			tree[idx][1] = 0;
			return;
		}
		else {
			tree[idx][0] = 0;
			tree[idx][1] = arr[start];
			return;
		}
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx][0] = tree[idx * 2][0] + tree[idx * 2 + 1][0];
	tree[idx][1] = tree[idx * 2][1] + tree[idx * 2 + 1][1];
}

LL abs(LL n) {
	if (n < 0) return -n;
	else return n;
}

LL interval_sum(int start, int end, int idx, int left, int right, int mode) {
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx][mode];

	int mid = (start + end) / 2;
	return interval_sum(start, mid, idx * 2, left, right, mode) + interval_sum(mid + 1, end, idx * 2 + 1, left, right, mode);
}

void update(int start, int end, int idx, int what, int value) {
	if (what < start || end < what) return;
	if (start == end) {
		if (start % 2 == 0) tree[idx][0] += value;
		else tree[idx][1] += value;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx][0] = tree[idx * 2][0] + tree[idx * 2 + 1][0];
	tree[idx][1] = tree[idx * 2][1] + tree[idx * 2 + 1][1];
}

int main(void) {
	int n, q;
	scanf("%d %d", &n, &q);
	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

	init(0, n - 1, 1);

	for (int i = 0; i < q; i++) {
		int mode, n1, n2;
		scanf("%d %d %d", &mode, &n1, &n2);
		if (mode == 1) {
			printf("%lld\n", abs(interval_sum(0, n - 1, 1, n1 - 1, n2 - 1, 0) - interval_sum(0, n - 1, 1, n1 - 1, n2 - 1, 1)));
		}
		else {
			update(0, n - 1, 1, n1 - 1, n2);
		}
	}
	return 0;
}