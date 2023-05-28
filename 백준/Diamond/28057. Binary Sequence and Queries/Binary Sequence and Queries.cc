#include <stdio.h>
#define SIZE 200005

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

	int range;
} Node;

char str[SIZE];
Node tree[SIZE * 4];

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

void update(int start, int end, int idx, int what, int value) {
	if (what < start || end < what) return;
	if (start == end) {
		bitset(start, end, idx, value + '0');
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

Node interval(int start, int end, int idx, int left, int right) {
	Node tmp;
	tmp.cnt0_left = 0; tmp.cnt0_left_pos[0] = start; tmp.cnt0_left_pos[1] = end;
	tmp.cnt0_right = 0; tmp.cnt0_right_pos[0] = start; tmp.cnt0_right_pos[1] = end;
	tmp.cnt0_all = 0; tmp.cnt0_all_pos[0] = start; tmp.cnt0_all_pos[1] = end;
	tmp.cnt1_left = 0; tmp.cnt1_left_pos[0] = start; tmp.cnt1_left_pos[1] = end;
	tmp.cnt1_right = 0; tmp.cnt1_right_pos[0] = start; tmp.cnt1_right_pos[1] = end;
	tmp.cnt1_all = 0; tmp.cnt1_all_pos[0] = start; tmp.cnt1_all_pos[1] = end;
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
		int mode;
		scanf("%d", &mode);

		if (mode == 1) {
			int p, t;
			scanf("%d %d", &p, &t);
			update(0, n - 1, 1, p - 1, t);
		}
		else {
			int l, r, x, y;
			scanf("%d %d %d %d", &l, &r, &x, &y);
			Node result;
			while (1) {
				if (l > r || (x == 0 && y == 0)) {
					printf("-1\n");
					break;
				}

				result = interval(0, n - 1, 1, l - 1, r - 1);
				int max0_cnt;
				int max0_pos[2];
				int max1_cnt;
				int max1_pos[2];

				if (result.cnt0_left >= result.cnt0_right && result.cnt0_left >= result.cnt0_all) {
					max0_cnt = result.cnt0_left;
					max0_pos[0] = result.cnt0_left_pos[0];
					max0_pos[1] = result.cnt0_left_pos[1];
				}
				else if (result.cnt0_right >= result.cnt0_left && result.cnt0_right >= result.cnt0_all) {
					max0_cnt = result.cnt0_right;
					max0_pos[0] = result.cnt0_right_pos[0];
					max0_pos[1] = result.cnt0_right_pos[1];
				}
				else {
					max0_cnt = result.cnt0_all;
					max0_pos[0] = result.cnt0_all_pos[0];
					max0_pos[1] = result.cnt0_all_pos[1];
				}

				if (result.cnt1_left >= result.cnt1_right && result.cnt1_left >= result.cnt1_all) {
					max1_cnt = result.cnt1_left;
					max1_pos[0] = result.cnt1_left_pos[0];
					max1_pos[1] = result.cnt1_left_pos[1];
				}
				else if (result.cnt1_right >= result.cnt1_left && result.cnt1_right >= result.cnt1_all) {
					max1_cnt = result.cnt1_right;
					max1_pos[0] = result.cnt1_right_pos[0];
					max1_pos[1] = result.cnt1_right_pos[1];
				}
				else {
					max1_cnt = result.cnt1_all;
					max1_pos[0] = result.cnt1_all_pos[0];
					max1_pos[1] = result.cnt1_all_pos[1];
				}

				//printf("(%d-%d) Max0 %lld (%d-%d) Max1 %lld (%d-%d)\n",l, r, max0_cnt, max0_pos[0], max0_pos[1], max1_cnt, max1_pos[0], max1_pos[1]);

				if (max0_cnt < x || max1_cnt < y) {
					printf("-1\n");
					break;
				}
				else if (max0_cnt == x && max1_cnt == y) {
					printf("%d %d\n", l, r);
					break;
				}
				else {
					// left - right relation check
					if (max0_pos[1] < max1_pos[0]) { // 0 - 1
						if (x != 0) l = max0_pos[0] + 1 + (max0_cnt - x);
						else l = max1_pos[0] + 1;

						if (y != 0) r = max1_pos[1] + 1 - (max1_cnt - y);
						else r = max0_pos[1] + 1;
					}
					else { // 1 - 0
						if (y != 0) l = max1_pos[0] + 1 + (max1_cnt - y);
						else l = max0_pos[0] + 1;

						if (x != 0) r = max0_pos[1] + 1 - (max0_cnt - x);
						else r = max1_pos[1] + 1;
					}
				}
			}
		}
	}
	return 0;
}