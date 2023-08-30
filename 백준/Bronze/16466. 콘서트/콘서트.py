import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(sorted(map(int, input().rstrip().split())))
now = 1
for i in range(n):
    if arr[i] != now:
        break
    else:
        now += 1
print(now)