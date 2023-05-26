#include <stdio.h>

// Array, Tree 사이즈 지정
#define SIZE 1000000

// 편의상 사용
typedef long long LL;

LL arr[SIZE]; // 배열
LL tree[SIZE * 4]; // 세그먼트 트리

void build(int start, int end, int idx) {
	if (start == end) {
		tree[idx] = arr[start];
		return;
	}

	int mid = (start + end) / 2;
	build(start, mid, idx * 2);
	build(mid + 1, end, idx * 2 + 1);

	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

void update(int start, int end, int idx, int what, LL value) {
	if (what < start || end < what) return;
	if (start == end) {
		tree[idx] = value;
		return;
	}

	int mid = (start + end) / 2;
	update(start, mid, idx * 2, what, value);
	update(mid + 1, end, idx * 2 + 1, what, value);
	
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

LL interval_sum(int start, int end, int idx, int left, int right) {
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	return interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right);
}

int main(void) {
	int n, m, k;
	scanf("%d %d %d", &n, &m, &k);
	
	// 수 저장
	for (int i = 0; i < n; i++)
		scanf("%lld", &arr[i]);

	// 세그먼트 트리 초기화
	build(0, n - 1, 1);

	/*
	build(0, n - 1, 1) -> 수가 arr[0] ~ arr[n-1]에 저장되었을 때 사용
	build(1, n, 1) -> 수가 arr[1] ~ arr[n]에 저장되었을 때 사용
	*/

	// 수 변경, 구간 합 구하기 수행
	for (int i = 0; i < m + k; i++) {
		int mode;
		scanf("%d", &mode);

		if (mode == 1) {
			int b;
			LL c;
			scanf("%d %lld", &b, &c);

			update(0, n - 1, 1, b - 1, c);
			/*
			update(0, n - 1, 1, b - 1, c) -> 수가 arr[0] ~ arr[b-1] ~ arr[n-1]에 저장되었을 때 사용
			update(1, n, 1, b, c) -> 수가 arr[1] ~ arr[b] ~ arr[n]에 저장되었을 때 사용
			*/
		}
		else { // mode == 2
			int b, c;
			scanf("%d %d", &b, &c);
			printf("%lld\n", interval_sum(0, n - 1, 1, b - 1, c - 1));
			/*
			interval_sum(0, n - 1, 1, b - 1, c - 1) -> 수가 arr[0] ~ arr[b-1] ~ arr[c-1] ~ arr[n-1]에 저장되었을 때 사용
			interval_sum(1, n, 1, b, c) -> 수가 arr[1] ~ arr[b] ~ arr[c] ~ arr[n]에 저장되었을 때 사용
			*/
		}
	}
	return 0;
}