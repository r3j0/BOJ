import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [0 for _ in range(n)]
for _ in range(m):
    order = list(map(int, input().rstrip().split()))
    if order[0] == 1: arr[order[1]-1] |= (1 << (order[2] - 1))
    elif order[0] == 2: arr[order[1]-1] &= (((1 << 20) - 1) - (1 << order[2] - 1))
    elif order[0] == 3: 
        arr[order[1]-1] <<= 1
        arr[order[1]-1] &= (1 << 20) - 1
    else: arr[order[1]-1] >>= 1
    

S = set()
for a in arr: S.add(a)
print(len(S))