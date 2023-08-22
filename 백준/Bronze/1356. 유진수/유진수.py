import sys
input = sys.stdin.readline

def mul(lis):
    now = 1
    for i in lis: now *= i
    return now

n = int(input().rstrip())
if len(str(n)) == 1: print('NO')
else:
    done = 0
    for i in range(1, len(str(n))):
        front = list(map(int, list(str(n)[:i])))
        end = list(map(int, list(str(n)[i:])))
        if mul(front) == mul(end): 
            done = 1
            break
    
    print('YES' if done else 'NO')