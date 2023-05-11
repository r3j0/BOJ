#include <stdio.h>
#include <string.h>
#define SIZE 100005

char str[SIZE];

int arr[SIZE] = { 0, };
int arrSize = 0;
int tree[SIZE * 4] = { 0, };
int sums[SIZE * 4] = { 0, };
int lazy[SIZE * 4] = { 0, };
int type = 0;
int min(int a, int b) {
	return (a < b ? a : b);
}

void init(int start, int end, int idx, int left) {
	if (start == end) {
		tree[idx] = arr[start];
		sums[idx] = left + arr[start];
		lazy[idx] = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2, left);
	init(mid + 1, end, idx * 2 + 1, left + tree[idx * 2]);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
	sums[idx] = min(sums[idx * 2], sums[idx * 2 + 1]);
}

void update_tree(int start, int end, int idx, int what) {
	if (what < start || end < what) return;
	if (start == end) {
		tree[idx] = (tree[idx] == 1) ? -1 : 1;
		type = tree[idx];
		return;
	}

	int mid = (start + end) / 2;
	update_tree(start, mid, idx * 2, what);
	update_tree(mid + 1, end, idx * 2 + 1, what);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

void update_lazy(int start, int end, int idx) {
	if (lazy[idx] != 0) {
		sums[idx] += (2 * lazy[idx]);
		if (start != end) {
			lazy[idx * 2] += lazy[idx];
			lazy[idx * 2 + 1] += lazy[idx];
		}
		lazy[idx] = 0;
	}
}
void update_sums(int start, int end, int idx, int left, int right) {
	update_lazy(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		sums[idx] += (2 * type);
		if (start != end) {
			lazy[idx * 2] += type;
			lazy[idx * 2 + 1] += type;
		}
		return;
	}

	int mid = (start + end) / 2;
	update_sums(start, mid, idx * 2, left, right);
	update_sums(mid + 1, end, idx * 2 + 1, left, right);
	sums[idx] = min(sums[idx * 2], sums[idx * 2 + 1]);
}

int main(void) {
	int n;
	scanf("%d", &n);
	getchar();
	fgets(str, SIZE, stdin);

	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == '(') arr[arrSize++] = 1;
		else if (str[i] == ')') arr[arrSize++] = -1;
	}

	init(0, arrSize - 1, 1, 0);
	int m;
	scanf("%d", &m);
	int f = 0;
	for (int i = 0; i < m; i++) {
		int num;
		scanf("%d", &num);

		if (num == 0) {
			if (tree[1] == 0 && sums[1] >= 0) printf("TAK\n");
			else printf("NIE\n");
		}
		else {
			update_tree(0, arrSize - 1, 1, num - 1);
			update_sums(0, arrSize - 1, 1, num - 1, arrSize - 1);
		}
	}
	
	return 0;
}