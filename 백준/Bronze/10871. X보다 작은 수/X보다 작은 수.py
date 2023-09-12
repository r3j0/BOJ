import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
           
for a in arr:
    if a < x: print(a, end=' ')