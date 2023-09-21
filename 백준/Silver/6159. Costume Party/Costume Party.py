import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] + arr[j] <= s: cnt += 1
print(cnt)