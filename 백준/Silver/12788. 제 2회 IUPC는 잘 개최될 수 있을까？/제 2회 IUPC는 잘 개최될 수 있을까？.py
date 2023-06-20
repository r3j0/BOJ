import sys
input = sys.stdin.readline

n = int(input().rstrip())
m, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

arr.sort()
now = m*k
cnt = 0
while now > 0 and len(arr) > 0:
    go = arr.pop()
    now -= go
    cnt += 1

if now <= 0: print(cnt)
else: print("STRESS")