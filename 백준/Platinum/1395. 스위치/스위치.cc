#include <stdio.h>
#define SIZE 100001

int tree[SIZE * 4] = { 0, };
int lazy[SIZE * 4] = { 0, };

void push(int start, int end, int idx) {
	if (lazy[idx] != 0) {
		tree[idx] = (end - start + 1) - tree[idx];
		if (start != end) {
			lazy[idx * 2] = (lazy[idx * 2] + 1) % 2;
			lazy[idx * 2 + 1] = (lazy[idx * 2 + 1] + 1) % 2;
		}
		lazy[idx] = 0;
	}
}

void update_range(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx] = (end - start + 1) - tree[idx];
		if (start != end) {
			lazy[idx * 2] = (lazy[idx * 2] + 1) % 2;
			lazy[idx * 2 + 1] = (lazy[idx * 2 + 1] + 1) % 2;
		}
		return;
	}

	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right);
	update_range(mid + 1, end, idx * 2 + 1, left, right);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

int interval_sum(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	return interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right);
}

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);
	while (m--) {
		int o, s, t;
		scanf("%d %d %d", &o, &s, &t);
		if (o == 0) {
			update_range(1, n, 1, s, t);
		}
		else { // o == 1
			printf("%d\n", interval_sum(1, n, 1, s, t));
		}
	}
	return 0;
}