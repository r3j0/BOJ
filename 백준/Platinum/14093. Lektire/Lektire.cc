#include <stdio.h>
#define SIZE 210000
typedef long long LL;

int arr[SIZE];
LL tree[SIZE * 4];

void init(int start, int end, int idx, int m) {
	if (start == end) {
		if (start < m) {
			arr[start] = 0;
			tree[idx] = 0;
			return;
		}
		else {
			arr[start - m] = start;
			tree[idx] = 1;
			return;
		}
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2, m);
	init(mid + 1, end, idx * 2 + 1, m);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

LL interval_sum(int start, int end, int idx, int left, int right) {
	if(end < left || right < start) return 0;
	if(left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	return interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right);
}

void update(int start, int end, int idx, int what, int value) {
	if(what < start || end < what) return;
	if(start == end) {
		tree[idx] += value;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);
	
	init(0, SIZE - 1, 1, m);

	int top = m - 1;
	LL result = 0;
	for(int i = 0; i < m; i++) {
		int num;
		scanf("%d", &num);

		result += interval_sum(0, SIZE - 1, 1, 0, arr[num - 1] - 1) + 1;
		update(0, SIZE - 1, 1, arr[num - 1], -1);
		update(0, SIZE - 1, 1, top, 1);
		arr[num - 1] = top--;
	}
	printf("%lld", result);
	return 0;
}