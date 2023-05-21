import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
now = 0
for i in range(n):
    if i == 0: now = arr[i]
    else: now ^= arr[i]

if now == 0: print('cubelover')
else: print('koosaga')