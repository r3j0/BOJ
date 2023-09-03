import sys
input = sys.stdin.readline

while True:
    arr = []
    n = int(input().rstrip())
    if n == 0: break
    result = 0
    while True:
        mode = input().rstrip()
        if mode == 'right on': 
            result = n
            break
        arr.append((n, 1 if mode == 'too high' else -1))
        n = int(input().rstrip())

    res = 0
    for an, amode in arr:
        if (result < an and amode == -1) or (result > an and amode == 1) or (result == an):
            res = 1
            break
    
    print('Stan is dishonest' if res == 1 else 'Stan may be honest')