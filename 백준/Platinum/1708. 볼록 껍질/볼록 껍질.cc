#include <stdio.h>
#define MAX_POINT 100005

typedef long long LL;

typedef struct _POINT {
    LL x;
    LL y;
} Point;

int n;
Point p[MAX_POINT];

Point tmp_p[MAX_POINT];
int stack[MAX_POINT];
int stack_size = 0;

LL CCW(Point p1, Point p2, Point p3) { return (p1.x*p2.y + p2.x*p3.y + p3.x*p1.y) - (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y); }

int isCcw(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) > 0) ? 1 : 0; }
int isCw(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) < 0) ? 1 : 0; }
int isLinear(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) == 0) ? 1 : 0; }

void MergeConvexHull(int start, int end) {
    int leftidx = start;
    int mid = (start + end) / 2;
    int rightidx = mid + 1;
    int allidx = start;

    while(leftidx <= mid && rightidx <= end) {
        if((p[leftidx].y - p[0].y) * (p[rightidx].x - p[0].x) < (p[leftidx].x - p[0].x) * (p[rightidx].y - p[0].y)) tmp_p[allidx++] = p[leftidx++];
        else if ((p[leftidx].y - p[0].y) * (p[rightidx].x - p[0].x) > (p[leftidx].x - p[0].x) * (p[rightidx].y - p[0].y)) tmp_p[allidx++] = p[rightidx++];
        else {
            if (p[leftidx].y < p[rightidx].y) tmp_p[allidx++] = p[leftidx++];
            else if (p[leftidx].y > p[rightidx].y) tmp_p[allidx++] = p[rightidx++];
            else {
                if (p[leftidx].x < p[rightidx].x) tmp_p[allidx++] = p[leftidx++];
                else tmp_p[allidx++] = p[rightidx++];
            }
        }
    }

    while(leftidx <= mid) tmp_p[allidx++] = p[leftidx++];
    while(rightidx <= end) tmp_p[allidx++] = p[rightidx++];

    for (int i = start; i <= end; i++) p[i] = tmp_p[i];
}

void MergeSortforConvexHull(int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        MergeSortforConvexHull(start, mid);
        MergeSortforConvexHull(mid + 1, end);
        MergeConvexHull(start, end);
    }
}

int convexHull() {
    Point minP = {p[0].x, p[0].y};
    int minIdx = 0;
    for (int i = 1; i < n; i++) {
        if (minP.y > p[i].y || (minP.y == p[i].y && minP.x > p[i].x)) {
            minP.x = p[i].x;
            minP.y = p[i].y;
            minIdx = i;
        }
    }
    p[minIdx].x = p[0].x;
    p[minIdx].y = p[0].y;
    p[0].x = minP.x;
    p[0].y = minP.y;

    MergeSortforConvexHull(1, n - 1);

    stack[stack_size++] = 0;
    stack[stack_size++] = 1;

    int now = 2;
    while (now < n) {
        while(stack_size >= 2) {
            int first = stack[stack_size - 2];
            int second = stack[stack_size - 1];
            stack_size -= 1;

            if (isCcw(p[first], p[second], p[now])) {
                stack[stack_size++] = second;
                break;
            }
        }

        stack[stack_size++] = now++;
    }

    return stack_size;
}

int main(void) {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &p[i].x, &p[i].y);
    }

    printf("%d", convexHull());
    return 0;
}