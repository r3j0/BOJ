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

int stree[SIZE * 4] = { 0, };
int slazy[SIZE * 4] = { 0, };

int btree[SIZE * 4] = { 0, };
int blazy[SIZE * 4] = { 0, };

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

void spush(int start, int end, int idx) {
	if (slazy[idx] != 0) {
		stree[idx] += (end - start + 1) * slazy[idx];
		if (start != end) {
			slazy[idx * 2] += slazy[idx];
			slazy[idx * 2 + 1] += slazy[idx];
		}
		slazy[idx] = 0;
	}
}

int sgetSum(int start, int end, int idx, int left, int right) {
	spush(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return stree[idx];

    int mid = (start + end) / 2;
	return sgetSum(start, mid, idx * 2, left, right) + sgetSum(mid + 1, end, idx * 2 + 1, left, right);
}

void supdate_range(int start, int end, int idx, int left, int right, int value) {
	spush(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
        slazy[idx] += value;
		spush(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	supdate_range(start, mid, idx * 2, left, right, value);
	supdate_range(mid + 1, end, idx * 2 + 1, left, right, value);
	stree[idx] = stree[idx * 2] + stree[idx * 2 + 1];
}

void bpush(int start, int end, int idx) {
	if (blazy[idx] != 0) {
		btree[idx] += (end - start + 1) * blazy[idx];
		if (start != end) {
			blazy[idx * 2] += blazy[idx];
			blazy[idx * 2 + 1] += blazy[idx];
		}
		blazy[idx] = 0;
	}
}

int bgetSum(int start, int end, int idx, int left, int right) {
	bpush(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return btree[idx];

    int mid = (start + end) / 2;
	return bgetSum(start, mid, idx * 2, left, right) + bgetSum(mid + 1, end, idx * 2 + 1, left, right);
}

void bupdate_range(int start, int end, int idx, int left, int right, int value) {
	bpush(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
        blazy[idx] += value;
		bpush(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	bupdate_range(start, mid, idx * 2, left, right, value);
	bupdate_range(mid + 1, end, idx * 2 + 1, left, right, value);
	btree[idx] = btree[idx * 2] + btree[idx * 2 + 1];
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

    int hug = 0;
	for (int i = 0; i < m; i++) {
		int mode;
		scanf("%d", &mode);

		if (mode == 1) {
			int i, w;
			scanf("%d %d", &i, &w);
            if (hug == 0) supdate_range(1, n, 1, start[i], end[i], w);
			else bupdate_range(1, n, 1, start[i], start[i], w);
		}
		else if (mode == 2){
			int i;
			scanf("%d", &i);
            printf("%d\n", sgetSum(1, n, 1, start[i], start[i]) + bgetSum(1, n, 1, start[i], end[i]));
		}
        else {
            if (hug == 0) hug = 1;
            else hug = 0;
        }
	}

	return 0;
}