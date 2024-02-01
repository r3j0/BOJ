#include <stdio.h>
#define MAX_POINT 2005

typedef long long LL;

typedef struct _POINT {
    LL x;
    LL y;
    int pn;
} Point;

int n;
Point p[MAX_POINT];

void pointSwap(Point* p1, Point* p2) {
    Point tmp = *p1;
    *p1 = *p2;
    *p2 = tmp;
}

LL CCW(Point p1, Point p2, Point p3) { return (p1.x*p2.y + p2.x*p3.y + p3.x*p1.y) - (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y); }

int isCcw(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) > 0) ? 1 : 0; }
int isCw(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) < 0) ? 1 : 0; }
int isLinear(Point p1, Point p2, Point p3) { return (CCW(p1, p2, p3) == 0) ? 1 : 0; }

LL PointToPointDistancePOW2(Point p1, Point p2) { return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y); }

int MergeConvexHullComp(Point pLeft, Point pRight, Point p0) {
    if((pLeft.y - p0.y) * (pRight.x - p0.x) < (pLeft.x - p0.x) * (pRight.y - p0.y)) return -1;
    else if ((pLeft.y - p0.y) * (pRight.x - p0.x) > (pLeft.x - p0.x) * (pRight.y - p0.y)) return 1;
    else {
        if (PointToPointDistancePOW2(pLeft, p0) < PointToPointDistancePOW2(pRight, p0)) return -1;
        else return 1;
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

void MergeConvexHull2(int start, int end) {
    Point tmp_p[MAX_POINT];
    int leftidx = start;
    int mid = (start + end) / 2;
    int rightidx = mid + 1;
    int allidx = start;

    while(leftidx <= mid && rightidx <= end) {
        if (MergeConvexHullComp(p[leftidx], p[rightidx], p[0]) > 0) tmp_p[allidx++] = p[leftidx++];
        else tmp_p[allidx++] = p[rightidx++];
    }

    while(leftidx <= mid) tmp_p[allidx++] = p[leftidx++];
    while(rightidx <= end) tmp_p[allidx++] = p[rightidx++];

    for (int i = start; i <= end; i++) p[i] = tmp_p[i];
}
void MergeSortforConvexHull2(int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        MergeSortforConvexHull2(start, mid);
        MergeSortforConvexHull2(mid + 1, end);
        MergeConvexHull2(start, end);
    }
}

int convexHull() {    
    Point minP = {p[0].x, p[0].y, p[0].pn};
    int minIdx = 0;
    for (int i = 1; i < n; i++) {
        if (minP.y > p[i].y || (minP.y == p[i].y && minP.x > p[i].x)) {
            minP.x = p[i].x;
            minP.y = p[i].y;
            minP.pn = p[i].pn;
            minIdx = i;
        }
    }
    p[minIdx].x = p[0].x;
    p[minIdx].y = p[0].y;
    p[minIdx].pn = p[0].pn;
    p[0].x = minP.x;
    p[0].y = minP.y;
    p[0].pn = minP.pn;

    MergeSortforConvexHull(1, n - 1);
    // 마지막 세점에서 직선화 될 수 있다는 점
    int find = n - 1;
    while (find - 1 > 0 && isLinear(p[0], p[find], p[find - 1])) find -= 1;
    //printf("%d\n", find);
    if (find != n - 1) MergeSortforConvexHull2(find, n - 1);

    for (int i = 0; i < n; i++) printf("%d ", p[i].pn);
    return -1;
}

int main(void) {
    int t;
    scanf("%d", &t);
    for (int tc = 0; tc < t; tc++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%lld %lld", &p[i].x, &p[i].y);
            p[i].pn = i;
        }

        int res = convexHull();
        printf("\n");
    }
    return 0;
}