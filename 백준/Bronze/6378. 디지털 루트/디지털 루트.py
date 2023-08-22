import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break

    while len(str(n)) != 1:
        now = 0
        for i in list(str(n)):
            now += int(i)
        n = now

    print(n)