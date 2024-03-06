import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(input().rstrip().split())
    now = arr[0]
    for i in range(1, n):
        if arr[0] >= arr[i] and now[0] >= arr[i]: now = arr[i] + now 
        else: now += arr[i]
    
    print(now)