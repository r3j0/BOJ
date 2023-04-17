import sys
input = sys.stdin.readline
n = int(input())
order = list(map(int, input().split()))

now = [0 for _ in range(n)]

for o in range(n):
    idx = 0
    cnt = 0
    while now[idx] != 0: idx += 1
    while cnt != order[o]:
        if now[idx] == 0: cnt += 1
        idx += 1
    while now[idx] != 0: idx += 1
    
    now[idx] = o + 1

print(' '.join(map(str, now)))