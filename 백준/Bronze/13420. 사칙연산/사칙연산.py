import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b = input().rstrip().split('=')
    if eval(a) == eval(b): print('correct')
    else: print('wrong answer')