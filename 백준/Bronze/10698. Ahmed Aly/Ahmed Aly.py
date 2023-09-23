import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    left, right = input().rstrip().split('=')
    if eval(left) == eval(right): print('Case %d: YES'%i)
    else: print('Case %d: NO'%i)