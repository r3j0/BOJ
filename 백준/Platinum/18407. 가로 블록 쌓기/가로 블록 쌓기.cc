#include <stdio.h>
#define SIZE 200005
typedef long long LL;

LL blocks[SIZE][2] = { 0, }; // 0 : start 1 : end

LL arr[SIZE * 2][3]; // 0 : pos, 1 : idx, 2 : start - end, 3 : rank
LL narr[SIZE * 2][3];
int arrSize = 0;

typedef struct _Node {
	int max_height;
	int lazy;
} Node;

Node tree[SIZE * 4];

Node merge(Node a, Node b) {
	Node tmp;
	if (a.max_height > b.max_height) tmp.max_height = a.max_height;
	else tmp.max_height = b.max_height;

	tmp.lazy = 0;
	return tmp;
}

void push(int start, int end, int idx) {
	tree[idx].max_height = tree[idx].lazy;

	if (start != end) {
		tree[idx * 2].lazy = tree[idx].lazy;
		tree[idx * 2 + 1].lazy = tree[idx].lazy;
	}
	tree[idx].lazy = 0;
}

int getMax(int start, int end, int idx, int left, int right) {
	if (tree[idx].lazy != 0) push(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx].max_height;

	int mid = (start + end) / 2;
	int r1 = getMax(start, mid, idx * 2, left, right);
	int r2 = getMax(mid + 1, end, idx * 2 + 1, left, right);
	if (r1 > r2) return r1;
	else return r2;
}

void update_range(int start, int end, int idx, int left, int right, int go) {
	if (tree[idx].lazy != 0) push(start, end, idx);

	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].lazy = go + 1;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_range(start, mid, idx * 2, left, right, go);
	update_range(mid + 1, end, idx * 2 + 1, left, right, go);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void merges(int start, int end) {
	int leftidx = start;
	int rightidx = (start + end) / 2 + 1;
	int allidx = start;

	while (leftidx <= (start + end) / 2 && rightidx <= end) {
		if (arr[leftidx][0] < arr[rightidx][0]) {
			for (int i = 0; i < 3; i++) narr[allidx][i] = arr[leftidx][i];
			allidx += 1; leftidx += 1;
		}
		else {
			for (int i = 0; i < 3; i++) narr[allidx][i] = arr[rightidx][i];
			allidx += 1; rightidx += 1;
		}
	}

	while (leftidx <= (start + end) / 2) {
		for (int i = 0; i < 3; i++) narr[allidx][i] = arr[leftidx][i];
		allidx += 1; leftidx += 1;
	}

	while (rightidx <= end) {
		for (int i = 0; i < 3; i++) narr[allidx][i] = arr[rightidx][i];
		allidx += 1; rightidx += 1;
	}

	for (int i = start; i <= end; i++) {
		for (int j = 0; j < 3; j++) arr[i][j] = narr[i][j];
	}
}

void merge_sort(int start, int end) {
	if (start < end) {
		int mid = (start + end) / 2;
		merge_sort(start, mid);
		merge_sort(mid + 1, end);
		merges(start, end);
	}
}

int main(void) {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		LL a, b;
		scanf("%lld %lld", &a, &b);

		arr[arrSize][0] = b - 1;
		arr[arrSize][1] = i;
		arr[arrSize][2] = 0;

		arrSize += 1;

		arr[arrSize][0] = a + b - 2;
		arr[arrSize][1] = i;
		arr[arrSize][2] = 1;

		arrSize += 1;
	}

	merge_sort(0, arrSize - 1);

	int rankcnt = 0;
	for (int i = 0; i < arrSize; i++) {
		if (i == 0) blocks[arr[i][1]][arr[i][2]] = 0;
		else {
			if (arr[i - 1][0] != arr[i][0]) rankcnt += 1;
			blocks[arr[i][1]][arr[i][2]] = rankcnt;
		}
	}

	for (int i = 0; i < n; i++) {
		int value = getMax(0, rankcnt, 1, blocks[i][0], blocks[i][1]);
		update_range(0, rankcnt, 1, blocks[i][0], blocks[i][1], value);
	}

	printf("%d", tree[1].max_height);

	return 0;
}