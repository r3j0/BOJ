import sys
input = sys.stdin.readline

n, m, l = map(int, input().rstrip().split())
arr = [0 for _ in range(n)]
arr[0] = 1
cnt = 0
now = 0
while max(arr) < m:
    if arr[now] % 2 == 1: 
        now = (now + l) % n
    else:
        now = now - l
        while now < 0: 
            now += n
    arr[now] += 1
    cnt += 1

print(cnt)