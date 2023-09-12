import sys
input = sys.stdin.readline

while True:
    a, b, c = input().rstrip().split()
    a = int(a)
    c = int(c)

    if a == c == 0: break
    if b == 'W':
        if a - c < -200: print('Not allowed')
        else: print(a-c)
    else:
        print(a+c)