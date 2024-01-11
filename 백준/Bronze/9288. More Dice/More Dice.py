import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    n = int(input().rstrip())
    print('Case %d:'%(i+1))
    for k in range(max(0, n-7), n//2):
        print('(%d,%d)'%(k+1, (n - (k+1))))