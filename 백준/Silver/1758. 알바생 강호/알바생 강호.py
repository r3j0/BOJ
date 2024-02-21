import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort(reverse=True)
res = 0
for i in range(n):
    res += max(arr[i] - i, 0)
print(res)