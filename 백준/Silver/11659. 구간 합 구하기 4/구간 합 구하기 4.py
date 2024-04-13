import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
sums = [0]
for i in range(n):
    sums.append(sums[-1] + arr[i])

for i in range(m):
    a, b = map(int, input().rstrip().split())
    print(sums[b] - sums[a-1])
    