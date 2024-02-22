import sys
input = sys.stdin.readline

a1, a0 = map(int, input().rstrip().split())
c = int(input().rstrip())
n0 = int(input().rstrip())

if (a1*n0+a0 >= c*n0 and a1 >= c): print(1)
else: print(0)