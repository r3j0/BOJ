#include <stdio.h>
#define SIZE 100001
typedef long long LL;

LL tree[SIZE * 4] = { 0, };
LL lazy[SIZE * 4] = { 0, };

int time_change(int hour, int minute, int second) {
	return second + (minute * 60) + (hour * 3600);
}

void push(int start, int end, int idx) {
	if (lazy[idx] != 0) {
		tree[idx] += (end - start + 1) * lazy[idx];

		if (start != end) {
			lazy[idx * 2] += lazy[idx];
			lazy[idx * 2 + 1] += lazy[idx];
		}

		lazy[idx] = 0;
	}
}

void update_range(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		lazy[idx] += 1;
		push(start, end, idx);

		return;
	}

	int mid = (start + end) / 2;

	update_range(start, mid, idx * 2, left, right);
	update_range(mid + 1, end, idx * 2 + 1, left, right);
	tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

LL interval_sum(int start, int end, int idx, int left, int right) {
	push(start, end, idx);

	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx];

	int mid = (start + end) / 2;
	return interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right);
}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int startHour, startMinute, startSecond, endHour, endMinute, endSecond;
		scanf("%d:%d:%d - %d:%d:%d", &startHour, &startMinute, &startSecond, &endHour, &endMinute, &endSecond);

		int start = time_change(startHour, startMinute, startSecond);
		int end = time_change(endHour, endMinute, endSecond);
		if (start > end) {
			update_range(0, SIZE - 1, 1, start, time_change(23, 59, 59));
			update_range(0, SIZE - 1, 1, 0, end);
		}
		else update_range(0, SIZE - 1, 1, start, end);
	}

	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		int startHour, startMinute, startSecond, endHour, endMinute, endSecond;
		scanf("%d:%d:%d - %d:%d:%d", &startHour, &startMinute, &startSecond, &endHour, &endMinute, &endSecond);

		int start = time_change(startHour, startMinute, startSecond);
		int end = time_change(endHour, endMinute, endSecond);
		if (start > end) {
			LL a1, a2, b1, b2;
			a1 = interval_sum(0, SIZE - 1, 1, start, time_change(23, 59, 59));
			a2 = interval_sum(0, SIZE - 1, 1, 0, end);
			b1 = (time_change(23, 59, 59) - start + 1);
			b2 = (end - 0 + 1);
			printf("%.10lf\n", (a1 + a2) / (double)(b1 + b2));
		}
		else printf("%.10lf\n", interval_sum(0, SIZE - 1, 1, start, end) / (double)(end - start + 1));
	}
	return 0;
}