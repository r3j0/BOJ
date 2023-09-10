import sys
input = sys.stdin.readline

while True:
    a, b, c, d = map(int, input().rstrip().split())
    if a == b == c == d == 0: break

    cnt = 0
    while not (a == b == c == d):
        cnt += 1
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
    
    print(cnt)