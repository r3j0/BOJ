import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

now = 1
for a in arr:
    if a == now:
        now += 1

print(n - (now - 1))