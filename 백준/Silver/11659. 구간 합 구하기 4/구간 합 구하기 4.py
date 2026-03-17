import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
s = [0]
for a in arr: s.append(s[-1] + a)

for _ in range(m):
    i, j = map(int, input().rstrip().split())
    print(s[j] - s[i-1])