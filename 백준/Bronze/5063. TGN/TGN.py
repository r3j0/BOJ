import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a,b,c = map(int, input().rstrip().split())
    if a == b-c: print('does not matter')
    elif a > b-c: print('do not advertise')
    else: print('advertise')