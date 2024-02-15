import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

cnt = 0
for i in range(n):
    if i == 0: cnt += 1
    elif arr[i] == arr[i-1]: cnt += 1
    else:
        for _ in range(cnt):
            print(i+1, end=' ')
        cnt = 1
for _ in range(cnt):
    print(-1, end=' ')