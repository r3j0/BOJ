import sys
input = sys.stdin.readline

def stringSum(a, b):
    idx = 1
    plus = 0
    go = ''
    while idx <= len(a) or idx <= len(b):
        if idx <= len(a): plus += int(a[-idx])
        if idx <= len(b): plus += int(b[-idx])
        go += str(plus % 10)
        plus //= 10
        idx += 1
    while plus != 0:
        go += str(plus % 10)
        plus //= 10
        
    return go[::-1]

n = int(input().rstrip())
if n <= 2: print(1)
else: 
    first = '1'
    second = '1'
    now = ''

    for i in range(3, n+1):
        now = stringSum(first, second)
        first = second
        second = now
    
    print(now)