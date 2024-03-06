import sys
input = sys.stdin.readline

n = int(input().rstrip())
a, b = map(int, input().rstrip().split())
c = int(input().rstrip())
sums = c
res = c // a
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort(reverse=True)

for i in range(n):
    sums += arr[i]
    res = max(res, sums//(a + b*(i+1)))
print(res)
