#include <stdio.h>
#include <stdlib.h>
#define SIZE 100001
typedef long long LL;

struct Node {
	int sibling;
	int child;
};
struct Node* seller[SIZE];

int start[SIZE];
int end[SIZE];
int visited = 1;

int tree[SIZE * 4] = { 0, };
int lazy[SIZE * 4] = { 0, };

void dfs(int now) {
	start[now] = visited++;
	if (seller[now]->child != -1) {
		dfs(seller[now]->child);
	}
	end[now] = visited - 1;
	if (seller[now]->sibling != -1) {
		dfs(seller[now]->sibling);
	}
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx] = 1;
		lazy[idx] = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

void push(int start, int end, int idx) {
	if (lazy[idx] != 0) {
		if (lazy[idx] == 1) tree[idx] = (end - start + 1) * lazy[idx];
		else if (lazy[idx] == -1) tree[idx] = 0;

		if (start != end) {
			lazy[idx * 2] = lazy[idx];
			lazy[idx * 2 + 1] = lazy[idx];
		}
		lazy[idx] = 0;
	}
}

int getVal(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	return getVal(start, mid, idx * 2, left, right) + getVal(mid + 1, end, idx * 2 + 1, left, right);
}

void update_range(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		lazy[idx] = value;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right, value);
	update_range(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

int main(void) {
	int n;
	scanf("%d", &n);	
	for (int i = 1; i <= n; i++) {
		seller[i] = (struct Node*)malloc(sizeof(struct Node));
		seller[i]->sibling = -1;
		seller[i]->child = -1;
	}

	int root = 1;
	for (int i = 1; i <= n; i++) {
		int parent;
		scanf("%d", &parent);
		if (parent != 0) {
			if (seller[parent]->child == -1) seller[parent]->child = i;
			else {
				int now = seller[parent]->child;
				while (seller[now]->sibling != -1) {
					now = seller[now]->sibling;
				}
				seller[now]->sibling = i;
			}
		}
		else root = i;
	}
	dfs(root);
	for (int i = 1; i <= n; i++) free(seller[i]);

	int m;
	scanf("%d", &m);

	init(1, n, 1);

	for (int i = 0; i < m; i++) {
		int mode;
		scanf("%d", &mode);

		if (mode == 1) {
			int i;
			scanf("%d", &i);
			update_range(1, n, 1, start[i] + 1, end[i], 1);
		}
		else if (mode == 2) {
			int i;
			scanf("%d", &i);
			update_range(1, n, 1, start[i] + 1, end[i], -1);
		}
		else {
			int i;
			scanf("%d", &i);
			printf("%d\n", getVal(1, n, 1, start[i] + 1, end[i]));
		}
	}

	return 0;
}