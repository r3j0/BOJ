import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    g = int(input())
    arr = list(map(int, input().split()))
    for a in arr:
        if arr.count(a) % 2 == 1:
            print('Case #%d:'%(i+1), a)
            break