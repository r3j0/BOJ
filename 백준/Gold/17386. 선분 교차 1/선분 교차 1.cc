#include <stdio.h>
#define MAX_POINT 100005

typedef long long LL;

typedef struct _POINT {
    LL x;
    LL y;
} Point;

int n;
Point p[MAX_POINT];

LL CCW(Point p1, Point p2, Point p3) { return (p1.x*p2.y + p2.x*p3.y + p3.x*p1.y) - (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y); }

int isCcw(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) > 0) ? 1 : 0; }
int isCw(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) < 0) ? 1 : 0; }
int isLinear(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) == 0) ? 1 : 0; }

int MergeConvexHullComp(Point pLeft, Point pRight, Point p0) {
    if((pLeft.y - p0.y) * (pRight.x - p0.x) < (pLeft.x - p0.x) * (pRight.y - p0.y)) return -1;
    else if ((pLeft.y - p0.y) * (pRight.x - p0.x) > (pLeft.x - p0.x) * (pRight.y - p0.y)) return 1;
    else {
        if (pLeft.y < pRight.y) return -1;
        else if (pLeft.y > pRight.y) return 1;
        else {
            if (pLeft.x < pRight.x) return -1;
            else return 1;
        }
    }
}
void MergeConvexHull(int start, int end) {
    Point tmp_p[MAX_POINT];
    int leftidx = start;
    int mid = (start + end) / 2;
    int rightidx = mid + 1;
    int allidx = start;

    while(leftidx <= mid && rightidx <= end) {
        if (MergeConvexHullComp(p[leftidx], p[rightidx], p[0]) < 0) tmp_p[allidx++] = p[leftidx++];
        else tmp_p[allidx++] = p[rightidx++];
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
    int stack[MAX_POINT];
    int stack_size = 0;

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
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &p[1].x, &p[1].y, &p[2].x, &p[2].y, &p[3].x, &p[3].y, &p[4].x, &p[4].y);
    LL p123 = CCW(p[1], p[2], p[3]);
    LL p124 = CCW(p[1], p[2], p[4]);
    LL p341 = CCW(p[3], p[4], p[1]);
    LL p342 = CCW(p[3], p[4], p[2]);
    if (((p123 <= 0 && p124 >= 0) || (p123 >= 0 && p124 <= 0)) && ((p341 <= 0 && p342 >= 0) || (p341 >= 0 && p342 <= 0))) printf("1");
    else printf("0");
    return 0;
}