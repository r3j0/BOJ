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

void push(int start, int end, int idx) {
	if (lazy[idx] != 0) {
		tree[idx] += (end - start + 1) * lazy[idx];
		if (start != end) {
			lazy[idx * 2] += lazy[idx];
			lazy[idx * 2 + 1] += lazy[idx];
		}
		lazy[idx] = 0;
	}
}

int getVal(int start, int end, int idx, int what, int* error) {
	push(start, end, idx);
	if (what < start || end < what) {
		*error = 1;
		return 0;
	}
	if (start == end) {
		*error = 0;
		return tree[idx];
	}

	int mid = (start + end) / 2;
	int e1 = 0;
	int q1 = getVal(start, mid, idx * 2, what, &e1);
	int e2 = 0;
	int q2 = getVal(mid + 1, end, idx * 2 + 1, what, &e2);

	if (e1 == 1 && e2 == 1) {
		*error = 1;
		return 0;
	}
	else {
		if (e1 != 1) return q1;
		else return q2;
	}
}

void update_range(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx] += (end - start + 1) * value;
		if (start != end) {
			lazy[idx * 2] += value;
			lazy[idx * 2 + 1] += value;
		}
		return;
	}

	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right, value);
	update_range(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);	
	for (int i = 1; i <= n; i++) {
		seller[i] = (struct Node*)malloc(sizeof(struct Node));
		seller[i]->sibling = -1;
		seller[i]->child = -1;
	}

	int root = 1;
	for (int i = 1; i <= n; i++) {
		int parent;
		scanf("%d", &parent);
		if (parent != -1) {
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

	for (int i = 0; i < m; i++) {
		int mode;
		scanf("%d", &mode);

		if (mode == 1) {
			int i, w;
			scanf("%d %d", &i, &w);
			update_range(1, n, 1, start[i], end[i], w);
		}
		else {
			int i, er;
			scanf("%d", &i);
			printf("%d\n", getVal(1, n, 1, start[i], &er));
		}
	}

	return 0;
}