#include <stdio.h>
#define SIZE 100001

int tree[SIZE * 4];

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx] = 1;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

int findKey(int start, int end, int idx, int key) {
	if (start == end) return start;
	if (tree[idx * 2] >= key) return findKey(start, (start + end) / 2, idx * 2, key);
	else return findKey((start + end) / 2 + 1, end, idx * 2 + 1, key - tree[idx * 2]);
}

void update(int start, int end, int idx, int what) {
	if (what < start || end < what) return;
	if (start == end) {
		tree[idx] -= 1;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what);
	update(mid + 1, end, idx * 2 + 1, what);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

void tree_debug(int s, int e, int i) {
	if (s == e) {
		printf("[%d] %d \n", s, tree[i]);
		return;
	}
	else {
		printf("[%d-%d] %d \n", s, e, tree[i]);
		int mid = (s + e) / 2;
		tree_debug(s, mid, i * 2);
		tree_debug(mid + 1, e, i * 2 + 1);
	}
}

int main(void) {
	int n, k;
	scanf("%d %d", &n, &k);
	
	init(1, n, 1);

	int now = k;
	printf("<");
	while (tree[1] != 0) {
		int res = findKey(1, n, 1, now);
		printf("%d", res);
		update(1, n, 1, res);
		if (tree[1] == 0) break;
		now = ((now + (k - 1)) - 1) % tree[1] + 1;
		//tree_debug(1, n, 1);
		printf(", ");
	}
	printf(">");
	return 0;
}