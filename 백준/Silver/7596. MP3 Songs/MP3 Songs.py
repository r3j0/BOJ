import sys
input = sys.stdin.readline

t = 1
while True:
    n = int(input().rstrip())
    if n == 0: break
    arr = [input().rstrip() for _ in range(n)]
    print(t)
    for a in list(sorted(arr)):
        print(a)
    t += 1