import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a = float(input().rstrip())
    print('%.10f'%(a/6))