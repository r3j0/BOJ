import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
arr = sorted(map(int, input().rstrip().split()))

for a in arr:
    if a <= l:
        l += 1
    else:
        break
print(l)