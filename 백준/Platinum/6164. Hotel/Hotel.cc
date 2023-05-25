#include <stdio.h>
#define SIZE 50005

typedef struct _Node {
	int mc_left;
	int ms_left;

	int mc_right;
	int ms_right;

	int mc_all;
	int ms_all;

	int range;

	int lazy;
} Node;

Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;

	if (a.range == a.mc_left && b.mc_left != 0) {
		if (a.mc_left >= a.range + b.mc_left) {
			tmp.mc_left = a.mc_left;
			tmp.ms_left = a.ms_left;
		}
		else {
			tmp.mc_left = a.range + b.mc_left;
			tmp.ms_left = a.ms_left;
		}
	}
	else {
		tmp.mc_left = a.mc_left;
		tmp.ms_left = a.ms_left;
	}

	if (b.range == b.mc_right && a.mc_right != 0) {
		if (a.mc_right + b.range >= b.mc_right) {
			tmp.mc_right = a.mc_right + b.range;
			tmp.ms_right = a.ms_right;
		}
		else {
			tmp.mc_right = b.mc_right;
			tmp.ms_right = b.ms_right;
		}
	}
	else {
		tmp.mc_right = b.mc_right;
		tmp.ms_right = b.ms_right;
	}

	// 1. a.right b.left 둘 다 0
	if (a.mc_right == 0 && b.mc_left == 0) {
		if (a.mc_all >= b.mc_all) {
			tmp.mc_all = a.mc_all;
			tmp.ms_all = a.ms_all;
		}
		else {
			tmp.mc_all = b.mc_all;
			tmp.ms_all = b.ms_all;
		}
	}
	// 2. a.right 가 0
	else if (a.mc_right == 0) {
		if (a.mc_all >= b.mc_all && a.mc_all >= b.mc_left) {
			tmp.mc_all = a.mc_all;
			tmp.ms_all = a.ms_all;
			if (tmp.mc_all == b.mc_all) tmp.ms_all = (tmp.ms_all < b.ms_all) ? tmp.ms_all : b.ms_all;
			if (tmp.mc_all == b.mc_left) tmp.ms_all = (tmp.ms_all < b.ms_left) ? tmp.ms_all : b.ms_left;
		}
		else if (b.mc_all >= a.mc_all && b.mc_all >= b.mc_left) {
			tmp.mc_all = b.mc_all;
			tmp.ms_all = b.ms_all;
			if (tmp.mc_all == a.mc_all) tmp.ms_all = (tmp.ms_all < a.ms_all) ? tmp.ms_all : a.ms_all;
			if (tmp.mc_all == b.mc_left) tmp.ms_all = (tmp.ms_all < b.ms_left) ? tmp.ms_all : b.ms_left;
		}
		else {
			tmp.mc_all = b.mc_left;
			tmp.ms_all = b.ms_left;
			if (tmp.mc_all == a.mc_all) tmp.ms_all = (tmp.ms_all < a.ms_all) ? tmp.ms_all : a.ms_all;
			if (tmp.mc_all == b.mc_all) tmp.ms_all = (tmp.ms_all < b.ms_all) ? tmp.ms_all : b.ms_all;
		}
	}
	// 3. b.left가 0
	else if (b.mc_left == 0) {
		if (a.mc_all >= b.mc_all && a.mc_all >= a.mc_right) {
			tmp.mc_all = a.mc_all;
			tmp.ms_all = a.ms_all;
			if (tmp.mc_all == b.mc_all) tmp.ms_all = (tmp.ms_all < b.ms_all) ? tmp.ms_all : b.ms_all;
			if (tmp.mc_all == a.mc_right) tmp.ms_all = (tmp.ms_all < a.ms_right) ? tmp.ms_all : a.ms_right;
		}
		else if (b.mc_all >= a.mc_all && b.mc_all >= a.mc_right) {
			tmp.mc_all = b.mc_all;
			tmp.ms_all = b.ms_all;
			if (tmp.mc_all == a.mc_all) tmp.ms_all = (tmp.ms_all < a.ms_all) ? tmp.ms_all : a.ms_all;
			if (tmp.mc_all == a.mc_right) tmp.ms_all = (tmp.ms_all < a.ms_right) ? tmp.ms_all : a.ms_right;
		}
		else {
			tmp.mc_all = a.mc_right;
			tmp.ms_all = a.ms_right;
			if (tmp.mc_all == a.mc_all) tmp.ms_all = (tmp.ms_all < a.ms_all) ? tmp.ms_all : a.ms_all;
			if (tmp.mc_all == b.mc_all) tmp.ms_all = (tmp.ms_all < b.ms_all) ? tmp.ms_all : b.ms_all;
		}
	}
	// 4. 연결됨
	else {
		if (a.mc_all >= b.mc_all && a.mc_all >= a.mc_right + b.mc_left) {
			tmp.mc_all = a.mc_all;
			tmp.ms_all = a.ms_all;
			if (tmp.mc_all == b.mc_all) tmp.ms_all = (tmp.ms_all < b.ms_all) ? tmp.ms_all : b.ms_all;
			if (tmp.mc_all == a.mc_right + b.mc_left) tmp.ms_all = (tmp.ms_all < a.ms_right) ? tmp.ms_all : a.ms_right;
		}
		else if (b.mc_all >= a.mc_all && b.mc_all >= a.mc_right + b.mc_left) {
			tmp.mc_all = b.mc_all;
			tmp.ms_all = b.ms_all;
			if (tmp.mc_all == a.mc_all) tmp.ms_all = (tmp.ms_all < a.ms_all) ? tmp.ms_all : a.ms_all;
			if (tmp.mc_all == a.mc_right + b.mc_left) tmp.ms_all = (tmp.ms_all < a.ms_right) ? tmp.ms_all : a.ms_right;
		}
		else {
			tmp.mc_all = a.mc_right + b.mc_left;
			tmp.ms_all = a.ms_right;
			if (tmp.mc_all == a.mc_all) tmp.ms_all = (tmp.ms_all < a.ms_all) ? tmp.ms_all : a.ms_all;
			if (tmp.mc_all == b.mc_all) tmp.ms_all = (tmp.ms_all < b.ms_all) ? tmp.ms_all : b.ms_all;
		}
	}

	tmp.range = a.range + b.range;
	tmp.lazy = 0;

	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].mc_left = 1;
		tree[idx].ms_left = start;

		tree[idx].mc_right = 1;
		tree[idx].ms_right = start;

		tree[idx].mc_all = 1;
		tree[idx].ms_all = start;

		tree[idx].range = 1;
		tree[idx].lazy = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void push(int start, int end, int idx) {
	if (tree[idx].lazy != 0) {
		if (tree[idx].lazy == -1) {
			tree[idx].mc_left = 0;
			tree[idx].ms_left = start;

			tree[idx].mc_right = 0;
			tree[idx].ms_right = start;

			tree[idx].mc_all = 0;
			tree[idx].ms_right = start;

			if (start != end) {
				tree[idx * 2].lazy = -1;
				tree[idx * 2 + 1].lazy = -1;
			}

			tree[idx].lazy = 0;
		}
		else { // 1
			tree[idx].mc_left = end - start + 1;
			tree[idx].ms_left = start;

			tree[idx].mc_right = end - start + 1;
			tree[idx].ms_right = start;

			tree[idx].mc_all = end - start + 1;
			tree[idx].ms_right = start;

			if (start != end) {
				tree[idx * 2].lazy = 1;
				tree[idx * 2 + 1].lazy = 1;
			}

			tree[idx].lazy = 0;
		}
	}
}

int mins(int a, int b) {
	if (a == -1 || b == -1) {
		if (a == -1 && b == -1) return -1;
		else if (a != -1) return a;
		else return b;
	}

	if (a < b) return a;
	else return b;
}

int find(int start, int end, int idx, int value) {
	push(start, end, idx);

	int now_start = -1;

	if (tree[idx].mc_left >= value) now_start = mins(now_start, tree[idx].ms_left);
	if (tree[idx].mc_all >= value) now_start = mins(now_start, tree[idx].ms_all);
	if (tree[idx].mc_right >= value) now_start = mins(now_start, tree[idx].ms_right);

	//printf("[%d-%d] search : %d\n", start, end, now_start);
	if (now_start == -1) return -1;
	if (start > end) return -1;
	if (start == end) return now_start;

	int mid = (start + end) / 2;
	int r1 = find(start, mid, idx * 2, value);
	if(r1 == -1) {
		int r2 = find(mid + 1, end, idx * 2 + 1, value);

		if (tree[idx * 2].mc_right + tree[idx * 2 + 1].mc_left >= value) {
			if (tree[idx * 2].mc_right == 0) now_start = mins(now_start, tree[idx * 2 + 1].ms_left);
			else now_start = mins(now_start, tree[idx * 2].ms_right);
		}

		return mins(now_start, mins(r1, r2));
	}
	else return mins(now_start, r1);
}

void update_range(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		if (value == 0) {
			tree[idx].lazy = -1;
			push(start, end, idx);
		}
		else if (value == 1) {
			tree[idx].lazy = 1;
			push(start, end, idx);
		}

		return;
	}

	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right, value);
	update_range(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

int main(void) {
	int n, m; scanf("%d %d", &n, &m);
	init(0, n - 1, 1);
	for (int i = 0; i < m; i++) {
		int mode;
		scanf("%d", &mode);
		if (mode == 1) {
			int x;
			scanf("%d", &x);
			int result = find(0, n - 1, 1, x);
			if (result != -1) update_range(0, n - 1, 1, result, result + x - 1, 0);
			printf("%d\n", result + 1);
		}
		else {
			int x, d;
			scanf("%d %d", &x, &d);
			update_range(0, n - 1, 1, x - 1, x - 1 + d - 1, 1);
		}
	}
	return 0;
}