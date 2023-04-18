#include <stdio.h>
#define SIZE 100001

int arr[SIZE];
int tree[SIZE * 4][2]; // min, max

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx][0] = start;
		tree[idx][1] = start;
		arr[start] = start;
		return;
	}
	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx][0] = (tree[idx * 2][0] < tree[idx * 2 + 1][0]) ? tree[idx * 2][0] : tree[idx * 2 + 1][0];
	tree[idx][1] = (tree[idx * 2][1] > tree[idx * 2 + 1][1]) ? tree[idx * 2][1] : tree[idx * 2 + 1][1];
}

int getBook(int start, int end, int idx, int what) {
	if (what < start || end < what) return -1;
	if (start == end) return arr[start];

	int mid = (start + end) / 2;
	int q1 = getBook(start, mid, idx * 2, what);
	int q2 = getBook(mid + 1, end, idx * 2 + 1, what);

	if (q1 == -1 && q2 == -1) return -1;
	else if (q1 != -1) return q1;
	else return q2;
}

void putBook(int start, int end, int idx, int what, int value) {
	if (what < start || end < what) return;
	if (start == end) {
		tree[idx][0] = value;
		tree[idx][1] = value;
		arr[start] = value;
		return;
	}

	int mid = (start + end) / 2;
	putBook(start, mid, idx * 2, what, value);
	putBook(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx][0] = (tree[idx * 2][0] < tree[idx * 2 + 1][0]) ? tree[idx * 2][0] : tree[idx * 2 + 1][0];
	tree[idx][1] = (tree[idx * 2][1] > tree[idx * 2 + 1][1]) ? tree[idx * 2][1] : tree[idx * 2 + 1][1];
}

int interval_min(int start, int end, int idx, int left, int right) {
	if (end < left || right < start) return -1;
	if (left <= start && end <= right) return tree[idx][0];

	int mid = (start + end) / 2;
	int q1 = interval_min(start, mid, idx * 2, left, right);
	int q2 = interval_min(mid + 1, end, idx * 2 + 1, left, right);
	if (q1 == -1 && q2 == -1) return -1;
	else if (q1 != -1 && q2 != -1) return (q1 < q2) ? q1 : q2;
	else if (q1 != -1) return q1;
	else return q2;
}

int interval_max(int start, int end, int idx, int left, int right) {
	if (end < left || right < start) return -1;
	if (left <= start && end <= right) return tree[idx][1];

	int mid = (start + end) / 2;
	int q1 = interval_max(start, mid, idx * 2, left, right);
	int q2 = interval_max(mid + 1, end, idx * 2 + 1, left, right);
	if (q1 == -1 && q2 == -1) return -1;
	else if (q1 != -1 && q2 != -1) return (q1 > q2) ? q1 : q2;
	else if (q1 != -1) return q1;
	else return q2;
}

int main(void) {
	int test;
	scanf("%d", &test);
	while (test--) {
		int n, k;
		scanf("%d %d", &n, &k);
		init(0, n - 1, 1);

		for (int i = 0; i < k; i++) {
			int q, a, b;
			scanf("%d %d %d", &q, &a, &b);

			if (q == 0) {
				int tmp1 = getBook(0, n - 1, 1, a);
				int tmp2 = getBook(0, n - 1, 1, b);
				putBook(0, n - 1, 1, a, tmp2);
				putBook(0, n - 1, 1, b, tmp1);
			}
			else {
				int mins = interval_min(0, n - 1, 1, a, b);
				int maxs = interval_max(0, n - 1, 1, a, b);
				// printf("%d %d / %d %d\n", mins, a, maxs, b);
				if (mins == a && maxs == b) printf("YES\n");
				else printf("NO\n");
			}
		}
	}
	return 0;
}