import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [-1 for _ in range(11)]
cnt = 0
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    if arr[a] == -1:
        arr[a] = b
    else:
        if (arr[a] == 1 and b == 0) or (arr[a] == 0 and b == 1):
            cnt += 1
            arr[a] = b
print(cnt)