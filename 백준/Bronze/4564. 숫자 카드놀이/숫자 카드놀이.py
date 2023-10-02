import sys
input = sys.stdin.readline

while True:
    tmp = int(input().rstrip())
    if tmp == 0: break

    print(tmp, end=' ')
    while len(str(tmp)) != 1:
        a = list(map(int, list(str(tmp))))
        now = a[0]
        for i in range(1, len(a)):
            now *= a[i]
        
        tmp = now
        print(tmp, end=' ')
    print()