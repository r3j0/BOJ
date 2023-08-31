import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break

    while len(str(n)) != 1:
        n = sum(map(int, list(str(n))))
    print(n)