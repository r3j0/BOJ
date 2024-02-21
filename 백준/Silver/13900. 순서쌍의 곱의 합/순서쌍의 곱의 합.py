import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
res = sum(arr)**2
for a in arr:
    res -= a**2

print(res//2)