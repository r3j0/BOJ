#include <stdio.h>
#define SIZE 100000
#define MIN_OVER 0
#define MAX_OVER 1000000001

int arr[SIZE];
int min_tree[SIZE * 4];
int max_tree[SIZE * 4];

void min_build(int start, int end, int idx) {
	if (start == end) {
		min_tree[idx] = arr[start];
		return;
	}

	int mid = (start + end) / 2;
	min_build(start, mid, idx * 2);
	min_build(mid + 1, end, idx * 2 + 1);

	min_tree[idx] = (min_tree[idx * 2] < min_tree[idx * 2 + 1] ? min_tree[idx * 2] : min_tree[idx * 2 + 1]);
}
void max_build(int start, int end, int idx) {
	if (start == end) {
		max_tree[idx] = arr[start];
		return;
	}

	int mid = (start + end) / 2;
	max_build(start, mid, idx * 2);
	max_build(mid + 1, end, idx * 2 + 1);

	max_tree[idx] = (max_tree[idx * 2] > max_tree[idx * 2 + 1] ? max_tree[idx * 2] : max_tree[idx * 2 + 1]);
}

int find_min(int start, int end, int idx, int left, int right) {
	if (end < left || right < start) return MAX_OVER;
	if (left <= start && end <= right) return min_tree[idx];

	int mid = (start + end) / 2;
	int n1 = find_min(start, mid, idx * 2, left, right);
	int n2 = find_min(mid + 1, end, idx * 2 + 1, left, right);

	return (n1 < n2 ? n1 : n2);
}

int find_max(int start, int end, int idx, int left, int right) {
	if (end < left || right < start) return MIN_OVER;
	if (left <= start && end <= right) return max_tree[idx];

	int mid = (start + end) / 2;
	int n1 = find_max(start, mid, idx * 2, left, right);
	int n2 = find_max(mid + 1, end, idx * 2 + 1, left, right);

	return (n1 > n2 ? n1 : n2);
}

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	min_build(0, n - 1, 1);
	max_build(0, n - 1, 1);

	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);

		printf("%d %d\n", find_min(0, n - 1, 1, a - 1, b - 1), find_max(0, n - 1, 1, a - 1, b - 1));
	}
	return 0;
}