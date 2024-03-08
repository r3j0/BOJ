import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break
    n -= 1
    idx = 0
    arr = []
    while n > 0:
        if n % 2 == 1: arr.append(3**idx)
        idx += 1
        n //= 2
    
    print('{ ' + ', '.join(map(str, arr)) + (' ' if len(arr) > 0 else '') + '}')