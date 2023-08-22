import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    arr = list(sorted(map(int, input().rstrip().split())))
    if arr[3] - arr[1] >= 4: print('KIN')
    else: print(sum(arr[1:4]))