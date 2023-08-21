import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    a, b, c = map(int, input().rstrip().split())

    print('Scenario #%d:'%i)
    if a**2 + b**2 == c ** 2 or a ** 2 == b ** 2 + c ** 2 or a ** 2 + c ** 2 == b ** 2: print('yes')
    else: print('no')

    if i != t: print()