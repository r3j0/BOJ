import sys
input = sys.stdin.readline

while True:
    try:
        a, b, c = list(sorted(map(int, input().rstrip().split())))
    except:
        break

    cnt = 0
    while not (a + 1 == b and b + 1 == c):
        if a + 1 == b:
            a = c - 1
        elif b + 1 == c:
            c = a + 1
        else:
            if abs(a-b) > abs(b-c):
                c = a + 1
            else:
                a = c - 1

        cnt += 1
        a, b, c = list(sorted([a, b, c]))
    
    print(cnt)