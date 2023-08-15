import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
now = []
now_reverse = []

for i in range(n):
    if arr[i] == 0: now.append(i+1)
    else:
        for _ in range(arr[i]):
            now_reverse.append(now[-1])
            del now[-1]
        now.append(i+1)
        for _ in range(arr[i]):
            now.append(now_reverse[-1])
            del now_reverse[-1]

print(' '.join(map(str, now)))