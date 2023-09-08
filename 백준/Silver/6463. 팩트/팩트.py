import sys
input = sys.stdin.readline

while True:
    n = 0
    try:
        n = int(input().rstrip())
    except:
        break

    now = 1
    for i in range(2, n+1):
        now *= i
        while now % 10 == 0:
            now //= 10
    
    print('%5d -> %s'%(n, now % 10))