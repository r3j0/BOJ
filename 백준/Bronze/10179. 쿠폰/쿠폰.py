import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = float(input().rstrip())
    print('$%.2f'%(n * 0.8))