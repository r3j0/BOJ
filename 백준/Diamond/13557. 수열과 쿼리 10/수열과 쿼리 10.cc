#include <stdio.h>
#define SIZE 100001
//#define DEBUG
typedef long long LL;

int arr[SIZE];

typedef struct _Node {
	LL lsum;
	LL rsum;
	LL allsum;

	LL sums;
} Node;

Node tree[SIZE * 4];

Node merge(Node Lnode, Node Rnode) {
	Node tmp;

	// L sum
	LL left_q1 = Lnode.lsum;
	LL left_q2 = Lnode.sums + Rnode.lsum;

	if (left_q1 > left_q2) tmp.lsum = left_q1; 
	else tmp.lsum = left_q2;

	// R sum
	LL right_q1 = Rnode.rsum;
	LL right_q2 = Lnode.rsum + Rnode.sums;

	if (right_q1 > right_q2) tmp.rsum = right_q1;
	else tmp.rsum = right_q2;

	// All sum
	LL all_q1 = Lnode.allsum;
	LL all_q2 = Rnode.allsum;
	LL all_q3 = Lnode.rsum + Rnode.lsum;

	if (all_q1 >= all_q2 && all_q1 >= all_q3) tmp.allsum = all_q1;
	else if (all_q2 >= all_q1 && all_q2 >= all_q3) tmp.allsum = all_q2;
	else tmp.allsum = all_q3;

	tmp.sums = Lnode.sums + Rnode.sums;
	return tmp;
}

void init(int start, int end, int idx) {
	if(start == end) {
		tree[idx].lsum = arr[start];
		tree[idx].rsum = arr[start];
		tree[idx].allsum = arr[start];
		tree[idx].sums = arr[start];
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

Node interval(int start, int end, int idx, int left, int right, int *error) {
	Node tmp;
	tmp.lsum = 0; tmp.rsum = 0; tmp.allsum = 0; tmp.sums = 0;
	if(end < left || right < start) {
		*error = 1;
		return tmp;
	}
	if(left <= start && end <= right) {
		*error = 0;
		return tree[idx];
	}

	int mid = (start + end) / 2;
	int e1 = 0;
	Node q1 = interval(start, mid, idx * 2, left, right, &e1);
	int e2 = 0;
	Node q2 = interval(mid + 1, end, idx * 2 + 1, left, right, &e2);

	if (e1 == 1 || e2 == 1) {
		if (e1 != 1) tmp = q1;
		else tmp = q2;
	}
	else tmp = merge(q1, q2);

	*error = 0;
	return tmp;
}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
	init(0, n - 1, 1);

	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		int x1, y1, x2, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		if (y1 >= x2) { // overlap case
			int e;
			LL result_max = 0;
			int result_assigned = 0;

			if (x1 == x2 && x2 == y1 && y1 == y2) { 
				Node tmp = interval(0, n - 1, 1, x1 - 1, x2 - 1, &e);
				if(result_assigned == 0 || result_max < tmp.sums) {
					result_assigned = 1;
					result_max = tmp.sums;
				}
			}
			else if (x1 == x2 && y1 == y2) {
				Node tmp = interval(0, n - 1, 1, x1 - 1, y1 - 1, &e);
				if(result_assigned == 0 || result_max < tmp.allsum) {
					result_assigned = 1;
					result_max = tmp.allsum;
				}
			}
			else if (x1 == x2) {
				Node result_mid = interval(0, n - 1, 1, x1 - 1, y1 - 1, &e);
				Node result_right = interval(0, n - 1, 1, y1, y2 - 1, &e);
				if(result_assigned == 0 || result_max < result_mid.rsum + result_right.lsum) {
					result_assigned = 1; 
					result_max = result_mid.rsum + result_right.lsum;
				}
				if(result_assigned == 0 || result_max < result_mid.allsum) {
					result_assigned = 1;
					result_max = result_mid.allsum;
				}	
			}
			else if (y1 == y2) {
				Node result_left = interval(0, n - 1, 1, x1 - 1, x2 - 2, &e);
				Node result_mid = interval(0, n - 1, 1, x2 - 1, y2 - 1, &e);
				if(result_assigned == 0 || result_max < result_left.rsum + result_mid.lsum) {
					result_assigned = 1; 
					result_max = result_left.rsum + result_mid.lsum;
				}
				if(result_assigned == 0 || result_max < result_mid.allsum) {
					result_assigned = 1;
					result_max = result_mid.allsum;
				}	
			}
			else if (y1 == x2) {
				Node result_left = interval(0, n - 1, 1, x1 - 1, y1 - 2, &e);
				Node result_mid = interval(0, n - 1, 1, y1 - 1, x2 - 1, &e);
				Node result_right = interval(0, n - 1, 1, x2, y2 - 1, &e);
				if(result_assigned == 0 || result_max < result_left.rsum + result_mid.sums + result_right.lsum) {
					result_assigned = 1; 
					result_max = result_left.rsum + result_mid.sums + result_right.lsum;	
				}
				if(result_assigned == 0 || result_max < result_left.rsum + result_mid.lsum) {
					result_assigned = 1; 
					result_max = result_left.rsum + result_mid.lsum;	
				}
				if(result_assigned == 0 || result_max < result_mid.rsum + result_right.lsum) {
					result_assigned = 1; 
					result_max = result_mid.rsum + result_right.lsum;	
				}
				if(result_assigned == 0 || result_max < result_mid.allsum) {
					result_assigned = 1;
					result_max = result_mid.allsum;
				}	
			}
			else {
				Node result_left = interval(0, n - 1, 1, x1 - 1, x2 - 2, &e);
				Node result_mid = interval(0, n - 1, 1, x2 - 1, y1 - 1, &e);
				Node result_right = interval(0, n - 1, 1, y1, y2 - 1, &e);
				if(result_assigned == 0 || result_max < result_left.rsum + result_mid.sums + result_right.lsum) {
					result_assigned = 1; 
					result_max = result_left.rsum + result_mid.sums + result_right.lsum;	
				}
				if(result_assigned == 0 || result_max < result_left.rsum + result_mid.lsum) {
					result_assigned = 1; 
					result_max = result_left.rsum + result_mid.lsum;	
				}
				if(result_assigned == 0 || result_max < result_mid.rsum + result_right.lsum) {
					result_assigned = 1; 
					result_max = result_mid.rsum + result_right.lsum;	
				}
				if(result_assigned == 0 || result_max < result_mid.allsum) {
					result_assigned = 1;
					result_max = result_mid.allsum;
				}
				
			}
			printf("%lld\n", result_max);
		}
		else {
			int e;
			Node result_left = interval(0, n - 1, 1, x1 - 1, y1 - 1, &e);
			Node result_mid = interval(0, n - 1, 1, y1, x2 - 2, &e);
			Node result_right = interval(0, n - 1, 1, x2 - 1, y2 - 1, &e);
			printf("%lld\n", result_left.rsum + result_mid.sums + result_right.lsum);
		}

	}
	return 0;
}