#include <stdio.h>
#include <stdlib.h>
#define SIZE 100005
#define max(a, b) (((a) > (b)) ? (a) : (b))
typedef long long LL;

LL arr[SIZE];
LL marr[SIZE];
LL tree[SIZE * 4];

void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx] = marr[start];
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1]);
}

LL interval_max(int start, int end, int idx, int left, int right, int* error) {
	if (end < left || right < start) {
		*error = 1;
		return 0;
	}
	if (left <= start && end <= right) {
		*error = 0;
		return tree[idx];
	}

	int mid = (start + end) / 2;
	int e1 = 0;
	LL r1 = interval_max(start, mid, idx * 2, left, right, &e1);
	int e2 = 0;
	LL r2 = interval_max(mid + 1, end, idx * 2 + 1, left, right, &e2);
	
	*error = 0;
	if (e1 == 1 || e2 == 1) {
		if (e1 != 1) return r1;
		else return r2;
	}
	else return max(r1, r2);
}

LL getVal(int start, int end, int idx, int what) {
	if (what < start || end < what) return 0;
	if (start == end) return tree[idx];

	int mid = (start + end) / 2;
	LL r1 = getVal(start, mid, idx * 2, what);
	LL r2 = getVal(mid + 1, end, idx * 2 + 1, what);

	if (r1 == 0) return r2;
	else return r1;
}

void update(int start, int end, int idx, int what) {
	if (what < start || end < what) return;
	if (start == end) {
		tree[idx] = marr[start];
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what);
	update(mid + 1, end, idx * 2 + 1, what);
	tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1]);
}

void tree_debug(int start, int end, int idx) {
	if (start == end) {
		printf("[%d] %lld (arr : %lld) (marr : %lld)\n", start, tree[idx], arr[start], marr[start]);
		return;
	}
	printf("[%d] %lld\n", start, tree[idx]);
	int mid = (start + end) / 2;
	tree_debug(start, mid, idx * 2);
	tree_debug(mid + 1, end, idx * 2 + 1);
}

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) scanf("%lld", &arr[i]);

	marr[0] = arr[0];
	for (int i = 1; i < n; i++) marr[i] = arr[i - 1] - arr[i];

	init(0, n - 1, 1);
	//tree_debug(0, n - 1, 1);

	for (int i = 0; i < m; i++) {
		int mode, l, r;
		scanf("%d %d %d", &mode, &l, &r);

		if (mode == 1) {
			if (l == r) printf("CS204\n");
			else {
				int error = 0;
				LL res = interval_max(0, n - 1, 1, l, r - 1, &error);

				if (res <= 0) printf("CS204\n");
				else printf("HSS090\n");
			}
		}
		else {
			LL tmp = arr[l - 1];
			arr[l - 1] = arr[r - 1];
			arr[r - 1] = tmp;

			if (l - 1 != 0) marr[l - 1] = arr[l - 2] - arr[l - 1];
			else marr[l - 1] = arr[l - 1];

			if (l - 1 != n - 1) marr[l] = arr[l - 1] - arr[l];
			
			if (r - 1 != 0) marr[r - 1] = arr[r - 2] - arr[r - 1];
			else marr[r - 1] = arr[r - 1];
			
			if (r - 1 != n - 1) marr[r] = arr[r - 1] - arr[r];

			update(0, n - 1, 1, l - 1);
			if(l <= n - 1) update(0, n - 1, 1, l);
			update(0, n - 1, 1, r - 1);
			if(r <= n - 1) update(0, n - 1, 1, r);

			//tree_debug(0, n - 1, 1);
		}
	}
	return 0;
}