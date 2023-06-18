#include <stdio.h>
#define SIZE 100001
typedef long long LL;

LL arr[SIZE] = {0,};
LL tree[SIZE * 4] = {0,};
LL lazy[SIZE * 4] = {0,};

void update_lazy(int start, int end, int idx) {
	if (lazy[idx] != 0) {
		tree[idx] += (end - start + 1) * lazy[idx];
		if (start != end) {
			lazy[idx * 2] += lazy[idx];
			lazy[idx * 2 + 1] += lazy[idx];
		}
		lazy[idx] = 0;
	}
}

void update_range(int start, int end, int idx, int left, int right) {
	update_lazy(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx] += (end - start + 1);
		if (start != end) {
			lazy[idx * 2] += 1;
			lazy[idx * 2 + 1] += 1;
		}
		return;
	}

	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right);
	update_range(mid + 1, end, idx * 2 + 1, left, right);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

void update_point(int start, int end, int idx, int what) {
	update_lazy(start, end, idx);

	if (what < start || end < what) return;
	if (start == end) {
		tree[idx] = 0;
		return;
	}

	int mid = (start + end) / 2;
	update_point(start, mid, idx * 2, what);
	update_point(mid + 1, end, idx * 2 + 1, what);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

LL getVal(int start, int end, int idx, int what) {
	update_lazy(start, end, idx);

	if (what < start || end < what) return 0;
	if (start == end) return tree[idx];

	int mid = (start + end) / 2;
	return getVal(start, mid, idx * 2, what) + getVal(mid + 1, end, idx * 2 + 1, what);
}

void tree_debug(int start, int end, int idx) {
	if (start == end) {
		printf("(%d) %d\n", start, tree[idx]);
		return;
	}
	else {
		printf("(%d-%d) %d\n", start, end, tree[idx]); 
		int mid = (start + end) / 2;
		tree_debug(start, mid, idx * 2);
		tree_debug(mid + 1, end, idx * 2 + 1);
		return;
	}
}

int main(void) {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int l, r;
		scanf("%d %d", &l, &r);
		if (l + 1 < r) update_range(0, SIZE - 1, 1, l, r - 2);
		LL cnt = getVal(0, SIZE - 1, 1, l - 1) + getVal(0, SIZE - 1, 1, r - 1);
		printf("%lld\n", cnt);

		update_point(0, SIZE - 1, 1, l - 1);
		update_point(0, SIZE - 1, 1, r - 1);

		//tree_debug(0, SIZE - 1, 1);
	}
	return 0;
}