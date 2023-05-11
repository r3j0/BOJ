#include <stdio.h>
#define SIZE 200005

int arr[SIZE];
typedef struct _Node {
	int min;
	int max;
	int cnt;

	int leftcnt;
	int rightcnt;
	int allcnt;
} Node;

Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;
	if (a.min < b.min) tmp.min = a.min;
	else tmp.min = b.min;
	if (a.max > b.max) tmp.max = a.max;
	else tmp.max = b.max;
	tmp.cnt = a.cnt + b.cnt;

	if (a.leftcnt == a.cnt) {
		if (a.leftcnt > a.cnt + b.leftcnt) tmp.leftcnt = a.leftcnt;
		else tmp.leftcnt = a.cnt + b.leftcnt;
	}
	else tmp.leftcnt = a.leftcnt;

	if (b.rightcnt == b.cnt) {
		if (b.rightcnt > b.cnt + a.rightcnt) tmp.rightcnt = b.rightcnt;
		else tmp.rightcnt = b.cnt + a.rightcnt;
	}
	else tmp.rightcnt = b.rightcnt;

	if (a.allcnt >= b.allcnt && a.allcnt >= a.rightcnt + b.leftcnt) tmp.allcnt = a.allcnt;
	else if (b.allcnt >= a.allcnt && b.allcnt >= a.rightcnt + b.leftcnt) tmp.allcnt = b.allcnt;
	else tmp.allcnt = a.rightcnt + b.leftcnt;

	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].min = arr[start];
		tree[idx].max = arr[start];
		tree[idx].cnt = 1;

		tree[idx].leftcnt = 0;
		tree[idx].rightcnt = 0;
		tree[idx].allcnt = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

int getVal(int start, int end, int idx, int what) {
	if (what < start || end < what) return -1;
	if (start == end) return tree[idx].max;

	int mid = (start + end) / 2;
	int n1 = getVal(start, mid, idx * 2, what);
	if (n1 == -1) return getVal(mid + 1, end, idx * 2 + 1, what);
	else return n1;
}

void update(int start, int end, int idx, int what, int value) {
	if (what < start || end < what) return;
	if (start == end) {
		tree[idx].max = value;
		tree[idx].min = value;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

Node interval(int start, int end, int idx, int left, int right) {
	Node tmp;
	tmp.max = -1;
	tmp.min = SIZE + 2;
	tmp.cnt = end - start + 1;
	tmp.leftcnt = 0;
	tmp.rightcnt = 0;
	tmp.allcnt = 0;
	if (right + 1 < tree[idx].min || tree[idx].max < left + 1) return tmp;
	if (left + 1 <= tree[idx].min && tree[idx].max <= right + 1) {
		tmp.max = tree[idx].max;
		tmp.min = tree[idx].min;
		tmp.leftcnt = end - start + 1;
		tmp.rightcnt = end - start + 1;
		tmp.allcnt = end - start + 1;
		//printf("[%d-%d] %d~%d -> %d\n", start, end, tree[idx].min, tree[idx].max, end - start + 1);
		return tmp;
	}
	if (start == end) return tmp;

	int mid = (start + end) / 2;
	tmp = merge(interval(start, mid, idx * 2, left, right), interval(mid + 1, end, idx * 2 + 1, left, right));
	//printf("[%d-%d] %d %d %d\n", start, end, tmp.leftcnt,tmp.rightcnt,tmp.allcnt);
	return tmp;
}

int main(void) {
	int n, m; 
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
	init(0, n - 1, 1);

	for (int i = 0; i < m; i++) {
		int mode, n1, n2;
		scanf("%d %d %d", &mode, &n1, &n2);

		if (mode == 1) {
			int x = getVal(0, n - 1, 1, n1 - 1);
			int y = getVal(0, n - 1, 1, n2 - 1);
			update(0, n - 1, 1, n1 - 1, y);
			update(0, n - 1, 1, n2 - 1, x);
		}
		else {
			Node result = interval(0, n - 1, 1, n1 - 1, n2 - 1);
			//printf("Left %d Right %d All %d\n", result.leftcnt, result.rightcnt, result.allcnt);
			int maxs;
			if (result.leftcnt >= result.rightcnt && result.leftcnt >= result.allcnt) maxs = result.leftcnt;
			else if (result.rightcnt >= result.leftcnt && result.rightcnt >= result.allcnt) maxs = result.rightcnt;
			else maxs = result.allcnt;

			if (maxs == n2 - n1 + 1) printf("YES\n");
			else printf("NO\n");
		}
	}
	return 0;
}