#include <stdio.h>
#define SIZE 100001
typedef long long LL;

LL arr[SIZE];

typedef struct _Node {
	LL leftValue; int leftCount;
	LL rightValue; int rightCount;
	LL allValue; int allCount;
	int intervalCount;
	LL lazy;
} Node;

Node tree[SIZE * 4];

Node merge(Node left, Node right) {
	Node tmp;
	
	// Left
	if (left.leftValue == right.leftValue && left.leftCount == left.intervalCount) {
		tmp.leftValue = left.leftValue;
		tmp.leftCount = left.intervalCount + right.leftCount;
	}
	else {
		tmp.leftValue = left.leftValue;
		tmp.leftCount = left.leftCount;
	}

	// Right
	if (right.rightValue == left.rightValue && right.rightCount == right.intervalCount) {
		tmp.rightValue = right.rightValue;
		tmp.rightCount = left.rightCount + right.intervalCount;
	}
	else {
		tmp.rightValue = right.rightValue;
		tmp.rightCount = right.rightCount;
	}

	// All
	LL q1 = left.allCount;
	LL q2 = right.allCount;
	LL q3 = left.rightCount + right.leftCount;

	if (left.rightValue == right.leftValue) {
		if (q3 >= q1 && q3 >= q2) {
			tmp.allValue = left.rightValue;
			tmp.allCount = left.rightCount + right.leftCount;
		}
		else if (q1 >= q2 && q1 >= q3) {
			tmp.allValue = left.allValue;
			tmp.allCount = left.allCount;
		}
		else  {
			tmp.allValue = right.allValue;
			tmp.allCount = right.allCount;
		}
	}
	else {
		if (q1 > q2) {
			tmp.allValue = left.allValue;
			tmp.allCount = left.allCount;
		}
		else {
			tmp.allValue = right.allValue;
			tmp.allCount = right.allCount;
		}
	}

	tmp.intervalCount = left.intervalCount + right.intervalCount;
	tmp.lazy = 0;
	return tmp;
}

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].leftValue = arr[start]; tree[idx].leftCount = 1;
		tree[idx].rightValue = arr[start]; tree[idx].rightCount = 1;
		tree[idx].allValue = arr[start]; tree[idx].allCount = 1;
		tree[idx].intervalCount = 1; 
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
		if (start == end) arr[start] += tree[idx].lazy;

		tree[idx].leftValue += tree[idx].lazy;
		tree[idx].rightValue += tree[idx].lazy;
		tree[idx].allValue += tree[idx].lazy;

		if (start != end) {
			tree[idx * 2].lazy += tree[idx].lazy;
			tree[idx * 2 + 1].lazy += tree[idx].lazy;
		}

		tree[idx].lazy = 0;
	}
}

Node interval_max(int start, int end, int idx, int left, int right) {
	push(start, end, idx);

	Node tmp;
	tmp.leftValue = 0; tmp.leftCount = -1;
	tmp.rightValue = 0; tmp.rightCount = -1;
	tmp.allValue = 0; tmp.allCount = -1;
	tmp.intervalCount = -1; tmp.lazy = 0;
	if (end < left || right < start) return tmp;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	Node q1 = interval_max(start, mid, idx * 2, left, right);
	Node q2 = interval_max(mid + 1, end, idx * 2 + 1, left, right);

	if (q1.intervalCount < 0 || q2.intervalCount < 0) {
		if (q1.intervalCount > 0) return q1;
		else return q2;
	}
	else tmp = merge(q1, q2);
	return tmp;
}

void update(int start, int end, int idx, int what, LL value) {
	push(start, end, idx);
	if (what < start || end < what) return;
	if (start == end) {
		arr[start] += value;
		tree[idx].leftValue += value;
		tree[idx].rightValue += value;
		tree[idx].allValue += value;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void update_range(int start, int end, int idx, int left, int right, LL value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		if (start == end) arr[start] += value;

		tree[idx].leftValue += value;
		tree[idx].rightValue += value;
		tree[idx].allValue += value;

		if (start != end) {
			tree[idx * 2].lazy += value;
			tree[idx * 2 + 1].lazy += value;
		}
		return;
	}
	
	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right, value);
	update_range(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%lld", &arr[i]);
	for (int i = n - 1; i >= 1; i--) arr[i] -= arr[i - 1];

	init(0, n - 1, 1);

	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		int mode;
		scanf("%d", &mode);

		if (mode == 1) {
			int a1, a2, a3, a4;
			scanf("%d %d %d %d", &a1, &a2, &a3, &a4);
			// 1. First x
			update(0, n - 1, 1, a1 - 1, a3);
			// 2. interval y
			if (a2 - a1 > 0) update_range(0, n - 1, 1, a1, a2 - 1, a4);
			// 3. end update
			if (a2 - a1 > 0) {
				if (a2 <= n - 1) update(0, n - 1, 1, a2, -(a3 + (LL)((LL)(a2 - a1) * a4)));
			}
			else {
				if (a2 <= n - 1) update(0, n - 1, 1, a2, -a3);
			}
		}
		else {
			int a1, a2;
			scanf("%d %d", &a1, &a2);
			Node result = interval_max(0, n - 1, 1, a1, a2 - 1);
			
			int result_max = result.leftCount;
			if (result_max < result.rightCount) result_max = result.rightCount;
			if (result_max < result.allCount) result_max = result.allCount;

			printf("%d\n", result_max + 1);
		}
	}

	return 0;
}