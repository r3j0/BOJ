import sys
input = sys.stdin.readline

while True:
    n = 0
    try:
        n = int(input().rstrip())
    except:
        break
    
    now = 1
    while now < n or now % n != 0:
        now *= 10
        now += 1
    
    print(len(str(now)))