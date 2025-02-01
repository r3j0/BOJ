#include <bits/stdc++.h>
using namespace std;

const int MAXN = 50000;
const int SEG_SIZE = 4 * MAXN + 10;

struct Node {
    int l, r;    // 구간 [l, r]
    int left;    // 구간의 왼쪽 끝부터 연속 free(1)인 방의 수
    int right;   // 구간의 오른쪽 끝부터 연속 free(1)인 방의 수
    int best;    // 구간 내 최대 연속 free인 방의 수
};

Node seg[SEG_SIZE];
int lazy[SEG_SIZE];  // lazy 값: -1이면 없음, 0이면 occupied, 1이면 free

// 세그먼트 트리 초기화 : 구간 [l, r]를 모두 free(1)로 초기화
void build(int idx, int l, int r) {
    seg[idx].l = l; 
    seg[idx].r = r;
    lazy[idx] = -1;
    if(l == r) {
        seg[idx].left = seg[idx].right = seg[idx].best = 1;
        return;
    }
    int mid = (l + r) / 2;
    build(idx*2, l, mid);
    build(idx*2+1, mid+1, r);
    int leftSize = seg[idx*2].r - seg[idx*2].l + 1;
    // 왼쪽 구간이 모두 free이면 오른쪽 자식의 left와 합침
    seg[idx].left = seg[idx*2].left;
    if(seg[idx*2].left == leftSize)
        seg[idx].left += seg[idx*2+1].left;
    int rightSize = seg[idx*2+1].r - seg[idx*2+1].l + 1;
    // 오른쪽 구간이 모두 free이면 왼쪽 자식의 right와 합침
    seg[idx].right = seg[idx*2+1].right;
    if(seg[idx*2+1].right == rightSize)
        seg[idx].right += seg[idx*2].right;
    // 구간 내 최대 free 길이는 왼쪽 자식, 오른쪽 자식, 두 자식을 연결한 경우 중 최댓값
    seg[idx].best = max({ seg[idx*2].best, seg[idx*2+1].best, seg[idx*2].right + seg[idx*2+1].left });
}

// lazy 값 전파: 현재 노드에 lazy가 있으면 자식 노드로 전파한다.
void push_down(int idx) {
    if(lazy[idx] != -1) {
        int val = lazy[idx];
        lazy[idx*2] = val;
        lazy[idx*2+1] = val;
        int mid = (seg[idx].l + seg[idx].r) / 2;
        int leftSize = mid - seg[idx].l + 1;
        int rightSize = seg[idx].r - mid;
        if(val == 1) { // free인 경우
            seg[idx*2].left = seg[idx*2].right = seg[idx*2].best = leftSize;
            seg[idx*2+1].left = seg[idx*2+1].right = seg[idx*2+1].best = rightSize;
        } else {       // occupied인 경우
            seg[idx*2].left = seg[idx*2].right = seg[idx*2].best = 0;
            seg[idx*2+1].left = seg[idx*2+1].right = seg[idx*2+1].best = 0;
        }
        lazy[idx] = -1;
    }
}

// 구간 [L, R]를 값 val로 업데이트 (val==1이면 free, val==0이면 occupied)
void update(int idx, int L, int R, int val) {
    if(seg[idx].r < L || seg[idx].l > R) return;
    if(L <= seg[idx].l && seg[idx].r <= R) {
        lazy[idx] = val;
        int size = seg[idx].r - seg[idx].l + 1;
        if(val == 1)
            seg[idx].left = seg[idx].right = seg[idx].best = size;
        else
            seg[idx].left = seg[idx].right = seg[idx].best = 0;
        return;
    }
    push_down(idx);
    update(idx*2, L, R, val);
    update(idx*2+1, L, R, val);
    int leftSize = seg[idx*2].r - seg[idx*2].l + 1;
    seg[idx].left = seg[idx*2].left;
    if(seg[idx*2].left == leftSize)
        seg[idx].left += seg[idx*2+1].left;
    int rightSize = seg[idx*2+1].r - seg[idx*2+1].l + 1;
    seg[idx].right = seg[idx*2+1].right;
    if(seg[idx*2+1].right == rightSize)
        seg[idx].right += seg[idx*2].right;
    seg[idx].best = max({ seg[idx*2].best, seg[idx*2+1].best, seg[idx*2].right + seg[idx*2+1].left });
}

// query(idx, D): 현재 세그먼트 트리 노드(idx) 구간 내에서 연속 free 구간 길이가 D 이상인
// 가장 왼쪽 위치를 반환한다. 만약 존재하지 않으면 -1을 반환.
int query(int idx, int D) {
    if(seg[idx].best < D) return -1;
    if(seg[idx].l == seg[idx].r) return seg[idx].l;
    push_down(idx);
    if(seg[idx*2].best >= D)
        return query(idx*2, D);
    if(seg[idx*2].right + seg[idx*2+1].left >= D)
        return seg[idx*2].r - seg[idx*2].right + 1;
    return query(idx*2+1, D);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    build(1, 1, N);
    while(M--){
        int type;
        cin >> type;
        if(type == 1) { // 체크인 요청: 1 D
            int D;
            cin >> D;
            int pos = query(1, D);
            if(pos == -1) {
                cout << 0 << "\n";
            } else {
                cout << pos << "\n";
                // 할당한 구간 [pos, pos+D-1]를 occupied(0)로 업데이트
                update(1, pos, pos + D - 1, 0);
            }
        } else { // 체크아웃 요청: 2 X D → 구간 [X, X+D-1]를 free(1)로 업데이트
            int X, D;
            cin >> X >> D;
            update(1, X, X + D - 1, 1);
        }
    }
    return 0;
}
