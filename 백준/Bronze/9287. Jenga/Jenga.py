import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    n = int(input().rstrip())
    done = 0
    for _ in range(n):
        string = input().rstrip()
        if string in ['100', '001', '000']: done = 1
    
    if done == 1: print('Case %d: Fallen'%i)
    else: print('Case %d: Standing'%i)