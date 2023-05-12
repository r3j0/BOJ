#include <stdio.h>
#include <assert.h>
#define SIZE 100010
typedef long long LL;

char str[SIZE];

LL arr[SIZE] = { 0, };
LL tree[SIZE * 4][2] = { 0, };
int type = 0;

LL min(LL a, LL b) {
	return (a < b ? a : b);
}

void init(int start, int end, int idx, int left) {
	if (start == end) {
		tree[idx][0] = arr[start];
		tree[idx][1] = left + arr[start];
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2, left);
	init(mid + 1, end, idx * 2 + 1, left + tree[idx * 2][0]);

	tree[idx][0] = tree[idx * 2][0] + tree[idx * 2 + 1][0];
	tree[idx][1] = min(tree[idx * 2][1], tree[idx * 2 + 1][1]);
}

LL interval_tree(int start, int end, int idx, int left, int right) {
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx][0];

	int mid = (start + end) / 2;
	return interval_tree(start, mid, idx * 2, left, right) + interval_tree(mid + 1, end, idx * 2 + 1, left, right);
}

LL interval_sums(int start, int end, int idx, int left, int right, int* error, int minus) {
	if (end < left || right < start) {
		*error = 1;
		return 0;
	}
	if (left <= start && end <= right) {
		*error = 0;
		//printf("[%d-%d] %d + %d \n",start, end, leftTree,tree[idx]);
		return tree[idx][1] - minus;
	}

	int mid = (start + end) / 2;
	int e1 = 0;
	int q1 = interval_sums(start, mid, idx * 2, left, right, &e1, minus);
	int e2 = 0;
	int q2 = interval_sums(mid + 1, end, idx * 2 + 1, left, right, &e2, minus);
	//printf("[%d-%d] %d (%d) %d (%d) \n", start,end,q1,e1,q2,e2);
	if (e1 == 1 || e2 == 1) {
		if (e1 != 1) return q1;
		else return q2;
	}
	else return min(q1, q2);
}
LL getVal(int start, int end, int idx, int what, int* er) {
	if (what < start || end < what) {
		*er = 1;
		return 0;
	}
	if (start == end) {
		*er = 0;
		return tree[idx][1];
	}

	int mid = (start + end) / 2;
	int e1 = 0;
	int q1 = getVal(start, mid, idx * 2, what, &e1);
	int e2 = 0;
	if (e1 == 1) return getVal(mid + 1, end, idx * 2 + 1, what, &e2);
	else return q1;
}

int main(void) {
	int n = 0, tmpn;
	scanf("%d", &tmpn);
	getchar();
	fgets(str, SIZE, stdin);

	for (int i = 0; str[i] != '\n' && str[i] != 0; i++) {
		if (str[i] == '(') arr[n++] = 1;
		else if (str[i] == ')') arr[n++] = -1;
	}

	init(0, n - 1, 1, 0);
	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		int a, b;
		
		int query = scanf("%d %d", &a, &b);	
		if (query == -1) {
			//assert(m == 100000 && i == 11);
			int now_i = i;
			while(now_i < m) {
				printf("0\n");
				now_i++;
			}
			break;
		}

		if (a <= 0 || b <= 0 || a > n || b > n || a == b) {
			printf("0\n");
			continue;
		}
		int now_a = (a < b) ? a : b;
		int now_b = (a < b) ? b : a;
		a = now_a; b = now_b;

		if ((b - a + 1) % 2 == 1) {
			printf("0\n");
			continue;
		}

		int it = interval_tree(0, n - 1, 1, a - 1, b - 1);
		int ise = 0;
		int minusVal = 0;
		if (a != 1) {
			int gve = 0;
			minusVal = getVal(0, n - 1, 1, a - 2, &gve);
			//printf("mV %d\n", minusVal);
		}
		int is = interval_sums(0, n - 1, 1, a - 1, b - 1, &ise, minusVal);
		//printf("%d %d / %d / %d\n", a, b, it, is);
		if (it == 0 && is >= 0) printf("1\n");
		else printf("0\n");
	}

	return 0;
}