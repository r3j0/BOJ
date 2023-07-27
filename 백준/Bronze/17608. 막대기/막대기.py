import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n): arr.append(int(input().rstrip()))
arr.reverse()
now = 0
res = 0
for a in arr:
    if a > now:
        now = a
        res += 1

print(res)