import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    a, b = map(int, input().rstrip().split())
    print('Scenario #%d:'%(i+1))
    print((b*(b+1)//2) - (a*(a-1)//2))
    print()