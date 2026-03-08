# 2042 : 구간 합 구하기
import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
arr = [0] + [int(input().rstrip()) for _ in range(n)]
tree = [0 for _ in range(n*4)]

def build(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return
    
    mid = (start + end) // 2
    build(start, mid, idx * 2)
    build(mid + 1, end, idx * 2 + 1)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

build(1, n, 1)

def interval_sum(start, end, idx, left, right):
    if end < left or right < start: return 0
    if left <= start and end <= right: return tree[idx]

    mid = (start + end) // 2
    return interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right)

def update(start, end, idx, k, x):
    if k < start or end < k: return
    if start == end:
        tree[idx] = x
        return
    
    mid = (start + end) // 2
    update(start, mid, idx * 2, k, x)
    update(mid + 1, end, idx * 2 + 1, k, x)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

for _ in range(m+k):
    a, b, c = map(int, input().rstrip().split())
    if a == 1:
        update(1, n, 1, b, c)
    else:
        print(interval_sum(1, n, 1, b, c))