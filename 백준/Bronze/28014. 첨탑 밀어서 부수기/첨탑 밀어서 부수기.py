import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
cnt = 1
for i in range(n - 1):
    if arr[i] <= arr[i+1]:
        cnt += 1
print(cnt)