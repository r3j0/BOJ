import sys
input = sys.stdin.readline

p, n = map(int, input().rstrip().split())
p = 200 - p
arr = list(sorted(map(int, input().rstrip().split())))

now = 0
idx = 0
while idx < n and now < p:
    now += arr[idx]
    idx += 1

print(idx)  