#include <stdio.h>
#define SIZE 100005

typedef struct _Node {
	int cnt0_left;
	int cnt0_left_pos[2];
	int cnt0_right;
	int cnt0_right_pos[2];
	int cnt0_all;
	int cnt0_all_pos[2];

	int cnt1_left;
	int cnt1_left_pos[2];
	int cnt1_right;
	int cnt1_right_pos[2];
	int cnt1_all;
	int cnt1_all_pos[2];

	int lazy;
	int range;
} Node;

char str[SIZE];
Node tree[SIZE * 4];

int max(int a, int b) {
	if (a > b) return a;
	else return b;
}

Node merge(Node a, Node b) {
	Node tmp;

	// 0 - left
	if (a.cnt0_left == a.range && b.cnt0_left != 0) {
		tmp.cnt0_left = a.range + b.cnt0_left;
		tmp.cnt0_left_pos[0] = a.cnt0_left_pos[0];
		tmp.cnt0_left_pos[1] = b.cnt0_left_pos[1];
	}
	else {
		tmp.cnt0_left = a.cnt0_left;
		tmp.cnt0_left_pos[0] = a.cnt0_left_pos[0];
		tmp.cnt0_left_pos[1] = a.cnt0_left_pos[1];
	}

	// 0 - right
	if (b.cnt0_right == b.range && a.cnt0_right != 0) {
		tmp.cnt0_right = a.cnt0_right + b.range;
		tmp.cnt0_right_pos[0] = a.cnt0_right_pos[0];
		tmp.cnt0_right_pos[1] = b.cnt0_right_pos[1];
	}
	else {
		tmp.cnt0_right = b.cnt0_right;
		tmp.cnt0_right_pos[0] = b.cnt0_right_pos[0];
		tmp.cnt0_right_pos[1] = b.cnt0_right_pos[1];
	}

	// 0 - all
	if (a.cnt0_all >= b.cnt0_all && a.cnt0_all >= a.cnt0_right + b.cnt0_left) {
		tmp.cnt0_all = a.cnt0_all;
		tmp.cnt0_all_pos[0] = a.cnt0_all_pos[0];
		tmp.cnt0_all_pos[1] = a.cnt0_all_pos[1];
	}
	else if (b.cnt0_all >= a.cnt0_all && b.cnt0_all >= a.cnt0_right + b.cnt0_left) {
		tmp.cnt0_all = b.cnt0_all;
		tmp.cnt0_all_pos[0] = b.cnt0_all_pos[0];
		tmp.cnt0_all_pos[1] = b.cnt0_all_pos[1];
	}
	else { // (a.cnt0_right + b.cnt0_left >= a.cnt0_all && a.cnt0_right + b.cnt0_left >= b.cnt0_all)
		tmp.cnt0_all = a.cnt0_right + b.cnt0_left;
		if (a.cnt0_right == 0 || b.cnt0_left == 0) {
			if (a.cnt0_right == 0 && b.cnt0_left == 0) {
				// ...?
				tmp.cnt0_all_pos[0] = a.cnt0_right_pos[0];
				tmp.cnt0_all_pos[1] = b.cnt0_left_pos[1];
			}
			else if (a.cnt0_right == 0) {
				tmp.cnt0_all_pos[0] = b.cnt0_left_pos[0];
				tmp.cnt0_all_pos[1] = b.cnt0_left_pos[1];
			}
			else if (b.cnt0_left == 0) {
				tmp.cnt0_all_pos[0] = a.cnt0_right_pos[0];
				tmp.cnt0_all_pos[1] = a.cnt0_right_pos[1];
			}
		}
		else {
			tmp.cnt0_all_pos[0] = a.cnt0_right_pos[0];
			tmp.cnt0_all_pos[1] = b.cnt0_left_pos[1];
		}
	}

	// 1 - left
	if (a.cnt1_left == a.range && b.cnt1_left != 0) {
		tmp.cnt1_left = a.range + b.cnt1_left;
		tmp.cnt1_left_pos[0] = a.cnt1_left_pos[0];
		tmp.cnt1_left_pos[1] = b.cnt1_left_pos[1];
	}
	else {
		tmp.cnt1_left = a.cnt1_left;
		tmp.cnt1_left_pos[0] = a.cnt1_left_pos[0];
		tmp.cnt1_left_pos[1] = a.cnt1_left_pos[1];
	}

	// 1 - right
	if (b.cnt1_right == b.range && a.cnt1_right != 0) {
		tmp.cnt1_right = a.cnt1_right + b.range;
		tmp.cnt1_right_pos[0] = a.cnt1_right_pos[0];
		tmp.cnt1_right_pos[1] = b.cnt1_right_pos[1];
	}
	else {
		tmp.cnt1_right = b.cnt1_right;
		tmp.cnt1_right_pos[0] = b.cnt1_right_pos[0];
		tmp.cnt1_right_pos[1] = b.cnt1_right_pos[1];
	}

	// 1 - all
	if (a.cnt1_all >= b.cnt1_all && a.cnt1_all >= a.cnt1_right + b.cnt1_left) {
		tmp.cnt1_all = a.cnt1_all;
		tmp.cnt1_all_pos[0] = a.cnt1_all_pos[0];
		tmp.cnt1_all_pos[1] = a.cnt1_all_pos[1];
	}
	else if (b.cnt1_all >= a.cnt1_all && b.cnt1_all >= a.cnt1_right + b.cnt1_left) {
		tmp.cnt1_all = b.cnt1_all;
		tmp.cnt1_all_pos[0] = b.cnt1_all_pos[0];
		tmp.cnt1_all_pos[1] = b.cnt1_all_pos[1];
	}
	else { // (a.cnt0_right + b.cnt0_left >= a.cnt0_all && a.cnt0_right + b.cnt0_left >= b.cnt0_all)
		tmp.cnt1_all = a.cnt1_right + b.cnt1_left;
		if (a.cnt1_right == 0 || b.cnt1_left == 0) {
			if (a.cnt1_right == 0 && b.cnt1_left == 0) {
				// ...?
				tmp.cnt1_all_pos[0] = a.cnt1_right_pos[0];
				tmp.cnt1_all_pos[1] = b.cnt1_left_pos[1];
			}
			else if (a.cnt1_right == 0) {
				tmp.cnt1_all_pos[0] = b.cnt1_left_pos[0];
				tmp.cnt1_all_pos[1] = b.cnt1_left_pos[1];
			}
			else if (b.cnt1_left == 0) {
				tmp.cnt1_all_pos[0] = a.cnt1_right_pos[0];
				tmp.cnt1_all_pos[1] = a.cnt1_right_pos[1];
			}
		}
		else {
			tmp.cnt1_all_pos[0] = a.cnt1_right_pos[0];
			tmp.cnt1_all_pos[1] = b.cnt1_left_pos[1];
		}
	}
	
	tmp.range = a.range + b.range;
	tmp.lazy = 0;
	return tmp;
}

void bitset(int start, int end, int idx, char val) {
	if (val == '0') {
		tree[idx].cnt0_left = 1;
		tree[idx].cnt0_left_pos[0] = start;
		tree[idx].cnt0_left_pos[1] = end;
		tree[idx].cnt0_right = 1;
		tree[idx].cnt0_right_pos[0] = start;
		tree[idx].cnt0_right_pos[1] = end;
		tree[idx].cnt0_all = 1;
		tree[idx].cnt0_all_pos[0] = start;
		tree[idx].cnt0_all_pos[1] = end;

		tree[idx].cnt1_left = 0;
		tree[idx].cnt1_left_pos[0] = start;
		tree[idx].cnt1_left_pos[1] = end;
		tree[idx].cnt1_right = 0;
		tree[idx].cnt1_right_pos[0] = start;
		tree[idx].cnt1_right_pos[1] = end;
		tree[idx].cnt1_all = 0;
		tree[idx].cnt1_all_pos[0] = start;
		tree[idx].cnt1_all_pos[1] = end;

		tree[idx].lazy = 0;
		tree[idx].range = 1;
	}
	else {
		tree[idx].cnt0_left = 0;
		tree[idx].cnt0_left_pos[0] = start;
		tree[idx].cnt0_left_pos[1] = end;
		tree[idx].cnt0_right = 0;
		tree[idx].cnt0_right_pos[0] = start;
		tree[idx].cnt0_right_pos[1] = end;
		tree[idx].cnt0_all = 0;
		tree[idx].cnt0_all_pos[0] = start;
		tree[idx].cnt0_all_pos[1] = end;

		tree[idx].cnt1_left = 1;
		tree[idx].cnt1_left_pos[0] = start;
		tree[idx].cnt1_left_pos[1] = end;
		tree[idx].cnt1_right = 1;
		tree[idx].cnt1_right_pos[0] = start;
		tree[idx].cnt1_right_pos[1] = end;
		tree[idx].cnt1_all = 1;
		tree[idx].cnt1_all_pos[0] = start;
		tree[idx].cnt1_all_pos[1] = end;

		tree[idx].lazy = 0;
		tree[idx].range = 1;
	}
}

void init(int start, int end, int idx) {
	if (start == end) {
		bitset(start, end, idx, str[start]);
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void swap(int* a, int* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void push(int start, int end, int idx) {
	if (tree[idx].lazy != 0) {
		swap(&tree[idx].cnt0_left, &tree[idx].cnt1_left);
		swap(&tree[idx].cnt0_left_pos[0], &tree[idx].cnt1_left_pos[0]);
		swap(&tree[idx].cnt0_left_pos[1], &tree[idx].cnt1_left_pos[1]);

		swap(&tree[idx].cnt0_right, &tree[idx].cnt1_right);
		swap(&tree[idx].cnt0_right_pos[0], &tree[idx].cnt1_right_pos[0]);
		swap(&tree[idx].cnt0_right_pos[1], &tree[idx].cnt1_right_pos[1]);

		swap(&tree[idx].cnt0_all, &tree[idx].cnt1_all);
		swap(&tree[idx].cnt0_all_pos[0], &tree[idx].cnt1_all_pos[0]);
		swap(&tree[idx].cnt0_all_pos[1], &tree[idx].cnt1_all_pos[1]);

		if (start != end) {
			tree[idx * 2].lazy = (tree[idx * 2].lazy + 1) % 2;
			tree[idx * 2 + 1].lazy = (tree[idx * 2 + 1].lazy + 1) % 2;
		}

		tree[idx].lazy = 0;
	}
}

void update(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].lazy = (tree[idx].lazy + 1) % 2;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, left, right);
	update(mid + 1, end, idx * 2 + 1, left, right);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

Node interval(int start, int end, int idx, int left, int right) {
	push(start, end, idx); 

	Node tmp;
	tmp.cnt0_left = 0; tmp.cnt0_left_pos[0] = start; tmp.cnt0_left_pos[1] = end;
	tmp.cnt0_right = 0; tmp.cnt0_right_pos[0] = start; tmp.cnt0_right_pos[1] = end;
	tmp.cnt0_all = 0; tmp.cnt0_all_pos[0] = start; tmp.cnt0_all_pos[1] = end;
	tmp.cnt1_left = 0; tmp.cnt1_left_pos[0] = start; tmp.cnt1_left_pos[1] = end;
	tmp.cnt1_right = 0; tmp.cnt1_right_pos[0] = start; tmp.cnt1_right_pos[1] = end;
	tmp.cnt1_all = 0; tmp.cnt1_all_pos[0] = start; tmp.cnt1_all_pos[1] = end;
	tmp.lazy = 0;
	tmp.range = end - start + 1;

	if (end < left || right < start) return tmp;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	return merge(interval(start, mid, idx * 2, left, right), interval(mid + 1, end, idx * 2 + 1, left, right));
}

int main(void) {
	int n, q;
	scanf("%d %d", &n, &q);
	scanf("%s", str);

	init(0, n - 1, 1);

	for (int i = 0; i < q; i++) {
		int mode, l, r;
		scanf("%d %d %d", &mode, &l, &r);

		if (mode == 1) {
			// Flip
			update(0, n - 1, 1, l - 1, r - 1);
		}
		else {
			// Combo
			Node result = interval(0, n - 1, 1, l - 1, r - 1);
			printf("%d\n", max(result.cnt0_left, max(result.cnt0_right, max(result.cnt0_all, max(result.cnt1_left, max(result.cnt1_right, result.cnt1_all))))));
		}
	}
	return 0;
}