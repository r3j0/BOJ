import sys
input = sys.stdin.readline

n = int(input().rstrip())
for k in range(n):
    arr = list(map(int, input().rstrip().split()))
    cnt = 0
    for i in range(10):
        if arr[i] == i % 5 + 1: cnt += 1
    
    if cnt == 10: 
        print(k+1)