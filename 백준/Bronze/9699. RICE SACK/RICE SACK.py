import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(1, n+1):
    arr = list(map(int, input().rstrip().split()))
    print('Case #%d: %d'%(i, max(arr)))