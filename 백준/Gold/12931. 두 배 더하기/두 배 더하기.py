import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

cnt = [[0, 0] for _ in range(n)]
for i in range(n):
    while arr[i] > 0:
        if arr[i] % 2 == 0: 
            arr[i] //= 2
            cnt[i][0] += 1
        else: 
            arr[i] -= 1
            cnt[i][1] += 1

max_value = cnt[0][0]
sum_value = cnt[0][1]
for i in range(1, n):
    max_value = max(cnt[i][0], max_value)
    sum_value += cnt[i][1]
print(max_value + sum_value)